#!/usr/bin/env python3

import argparse
import csv
import json
import multiprocessing
import os
import subprocess
import sys
import tempfile
import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk
from typing import Set, List, Optional, NewType, Tuple, Iterable, Any, Callable

import requests
from requests.auth import AuthBase

Registry = NewType("Registry", str)
Repository = NewType("Repository", str)
Tag = NewType("Tag", str)
Digest = NewType("Digest", str)
AuthToken = NewType("AuthToken", str)


def main(argv):

    # first positional arg is the command, the rest depends on the command

    parser = argparse.ArgumentParser(
        description="""
            Tool for viewing and managing the containers in a remote Docker registry.
            Uses the authentication credentials in ~/.docker/config.json. Use `docker login` to set them, if required.
        """
    )
    parser.add_argument("command", choices=["manage"])

    args = parser.parse_args(argv[:1])

    if args.command == "manage":
        manage(argv[1:])


def manage(argv):

    # first positional arg is the registry
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", choices=read_registries())
    parser.add_argument("--repository", required=False)
    parser.add_argument("--sort", choices=["digest", "tag"], default="digest")

    args = parser.parse_args(argv)
    registry = args.registry

    # read credentials from ~/.docker/config.json
    auth = read_credentials(registry)

    images = list_images(registry, auth, lambda repo: args.repository is None or repo == args.repository)
    if args.sort == "digest":
        images.sort(key=lambda image: (image.repository, image.digest, image.tag))
    elif args.sort == "tag":
        images.sort(key=lambda image: (image.repository, image.tag, image.digest))

    selected = select_interactively(images)
    print_list("selected", selected)

    # delete the selected images
    concurrent_starmap(delete_image, [(registry, digest, auth) for digest in selected])

    print("""Remote images deleted. Don't forget to collect garbage, e.g. using:
    docker exec dockreg_registry_1 bin/registry garbage-collect --delete-untagged /etc/docker/registry/config.yml""")


def read_registries() -> Set[Registry]:
    """Read the list of registries from ~/.docker/config.json."""
    config = json.load(open(os.path.expanduser("~/.docker/config.json")))
    return set(config["auths"].keys())


def read_credentials(registry: Registry) -> AuthToken:
    """Read the credentials for the given registry from ~/.docker/config.json."""
    config = json.load(open(os.path.expanduser("~/.docker/config.json")))
    auth = config["auths"][registry]["auth"]
    if not isinstance(auth, str):
        raise ValueError("auth is not a string")
    print(f"{registry} auth: {auth[0:3]}{'*' * (len(auth)-3)}")
    return AuthToken(auth)


class HTTPBasicAuthEncoded(AuthBase):
    """Attaches HTTP Basic Authentication to the given Request object.
    Uses an already-encoded username:password string."""

    def __init__(self, token):
        self.token = token

    def __eq__(self, other):
        return self.token == getattr(other, "token", None)

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.headers["Authorization"] = f"Basic {self.token}"
        return r


@dataclass
class Image:
    repository: Repository
    tag: Tag
    digest: Digest
    # more: Any


ImageDigest = tuple[Repository, Digest]


def list_images(registry: Registry, auth: AuthToken, include_repo: Callable[[str], bool] = lambda _: True) -> List[Image]:
    """List all images in the given registry, using the HTTP API."""

    # List all repositories (effectively images):
    #
    # curl -X GET https://myregistry:5000/v2/_catalog
    # > {"repositories":["redis","ubuntu"]}
    # List all tags for a repository:
    #
    # curl -X GET https://myregistry:5000/v2/ubuntu/tags/list
    # > {"name":"ubuntu","tags":["14.04"]}
    # If the registry needs authentication you have to specify username and password in the curl command
    #
    # curl -X GET -u <user>:<pass> https://myregistry:5000/v2/_catalog
    # curl -X GET -u <user>:<pass> https://myregistry:5000/v2/ubuntu/tags/list

    basic_auth = HTTPBasicAuthEncoded(auth)

    repos = [
        repo for repo in
        requests.get(f"https://{registry}/v2/_catalog", auth=basic_auth).json()["repositories"]
        if include_repo(repo)
    ]
    print(repos)

    with_tags = [{
        "repository": repo,
        "tags": requests.get(f"https://{registry}/v2/{repo}/tags/list", auth=basic_auth).json()["tags"],
    } for repo in repos]
    print(with_tags)

    fetch_tasks = [(registry, repo["repository"], tag, basic_auth) for repo in with_tags for tag in repo["tags"]]

    images: list[Image] = concurrent_starmap(fetch_tag_info, fetch_tasks)

    return images


# def concurrent_map(func: Callable[T, R], iterable: Iterable[T]) -> List[R]: - TODO make work
def concurrent_starmap(func, iterable):
    pool = multiprocessing.Pool(8)
    return pool.starmap(func, iterable)


def fetch_tag_info(registry: Registry, repo: Repository, tag: Tag, basic_auth: HTTPBasicAuthEncoded) -> Image:

    # runtime type checks
    if not isinstance(repo, str):
        raise ValueError(f"repo is not a string: {repr(repo)}")
    if not isinstance(tag, str):
        raise ValueError(f"tag is not a string: {repr(tag)}")

    info_resp = requests.get(f"https://{registry}/v2/{repo}/manifests/{tag}", auth=basic_auth,
                             headers={"Accept": "application/vnd.docker.distribution.manifest.v2+json"})
    # print(f"{repo}/{tag} info: {info_resp}")
    image = Image(
        repository=repo,
        tag=tag,
        digest=Digest(info_resp.headers["Docker-Content-Digest"]),
        # more=info_resp.json(),
    )
    print(image)
    return image


def delete_image(registry: Registry, imdi: ImageDigest, auth: AuthToken) -> tuple[ImageDigest, bool]:
    repo, digest = imdi
    basic_auth = HTTPBasicAuthEncoded(auth)
    url = f"https://{registry}/v2/{repo}/manifests/{digest}"
    print(f"DELETE {url}")
    resp = requests.delete(url, auth=basic_auth)
    if resp.status_code == 202:
        print(f"Deleted {repo}@{digest}")
        return imdi, True
    else:
        print(f"Failed to delete {repo}@{digest}: {resp.status_code} {resp.text}")
        return imdi, False


def select_interactively(images: List[Image]) -> Set[ImageDigest]:
    return select_interactively_csv(images)


def select_interactively_csv(images: List[Image]) -> Set[ImageDigest]:
    """
    Write the list of images to a temporary CSV file, then open it in LibreOffice Calc.
    Wait for the user to mark items for deletion by putting an X in the first column,
    then read the CSV file again and return the list of deleted items.
    Abort if the mtime of the CSV file was not changed.
    """
    outfile = tempfile.NamedTemporaryFile(suffix=".csv")
    with open(outfile.name, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["delete", "repository", "tag", "digest", "other tags"])
        for image in images:
            writer.writerow([
                "X", image.repository, image.tag, image.digest,
                ", ".join(oi.tag for oi in images if oi.digest == image.digest and oi.tag != image.tag),
            ])

    mtime = os.path.getmtime(outfile.name)

    subprocess.check_call([
        "libreoffice",
        # launch a completely standalone LibreOffice Calc instance, i.e. not affecting or affected by the user's current Calc instance
        f"-env:UserInstallation=file://{tempfile.mkdtemp()}",
        "--calc", outfile.name,
    ])

    if os.path.getmtime(outfile.name) == mtime:
        raise RuntimeError("The CSV file was not modified, aborting.")

    with open(outfile.name) as f:
        reader = csv.reader(f)
        next(reader)
        result: List[Tuple[str, Image]] = [(row[0], Image(*row[1:4])) for row in reader]
    print_list("result", result)

    deletes: List[Image] = [image for (delcol, image) in result if delcol == "X"]
    print_list("delete", deletes)

    # if multiple images have the same digest, only delete it if all of them are marked for deletion
    def delkey(i: Image) -> Tuple[Repository, Tag]:
        return i.repository, i.tag

    # TODO verify that the result list equals the original list (except for the first column),
    #      then calcing preserve is as simple as collecting the items with delcol == ""

    delete_keys = {delkey(img) for img in deletes}
    print_list("delete_keys", delete_keys)
    preserve = [img for img in images if delkey(img) not in delete_keys]
    print_list("preserve", preserve)
    preserve_digests = {image.digest for image in preserve}
    print(f"{preserve_digests=}")
    really_delete: Set[ImageDigest] = {(img.repository, img.digest) for img in deletes if img.digest not in preserve_digests}
    print_list("really_delete", really_delete)

    return really_delete


# similar to select_interactively_csv, but instead of CSV, write an ODS file with actual interactive checkboxes instead of "X" marks
def select_interactively_ods(images: List[Image]) -> Set[ImageDigest]:
    # https://pypi.org/project/pyexcel-ods3/
    raise NotImplementedError()


def print_list(label: str, lst: Iterable[Any]):
    print(f"{label}:")
    for item in lst:
        print(f"  {item}")


def select_interactively_tk(images: List[Image]) -> List[Image]:
    """Show the list of images in any kind of interactive (G)UI, where the user can make selections and mark/unmark them, and with an option to delete them or to abort the operation."""

    # use tkinter

    root = tk.Tk()
    root.title("Select images to delete")
    root.geometry("1600x900")

    selection_vars = [tk.BooleanVar(value=True) for _ in images]

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("delete", "repository", "tag", "digest"), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    tree.heading("delete", text="Delete")
    tree.heading("repository", text="Repository")
    tree.heading("tag", text="Tag")
    tree.heading("digest", text="Digest")

    tree.column("delete", width=50, anchor=tk.CENTER)
    tree.column("repository", width=200)
    tree.column("tag", width=100)
    tree.column("digest", width=200)

    for image, selection_var in zip(images, selection_vars):
        # show selection checkbox
        tree.insert("", tk.END, values=(tk.Checkbutton(tree, variable=selection_var), image.repository, image.tag, image.digest))

    tree.bind("<Button-1>", lambda event: tree.focus(tree.identify_row(event.y)))

    def toggle_selection(event):
        item = tree.focus()
        if item:
            selection_vars[int(item)].set(not selection_vars[int(item)].get())

    tree.bind("<space>", toggle_selection)

    retval: Optional[List[Image]] = None

    def delete_selected():
        nonlocal retval
        retval = [image for image, var in zip(images, selection_vars) if var.get()]
        root.quit()

    def abort():
        root.quit()

    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X, expand=True)

    delete_button = tk.Button(button_frame, text="Delete selected", command=delete_selected)
    delete_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

    abort_button = tk.Button(button_frame, text="Abort", command=abort)
    abort_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # run the GUI
    root.mainloop()

    if retval is None:
        raise RuntimeError("GUI was aborted")
    else:
        return retval


# import tkinter as tk
#
# def select_items():
#     selected_items = [item for item in items_list if item_vars[item].get() == 1]
#     print(selected_items)
#
# root = tk.Tk()
# root.title("Item Selector")
#
# items_list = ["item1", "item2", "item3", "item4", "item5"]
# item_vars = {}
#
# for item in items_list:
#     item_vars[item] = tk.IntVar()
#     tk.Checkbutton(root, text=item, variable=item_vars[item]).pack()
#
# tk.Button(root, text="Select", command=select_items).pack()
#
# root.mainloop()

if __name__ == '__main__':
    main(sys.argv[1:])
