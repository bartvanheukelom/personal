#!/bin/bash

set -e

pushd repos

for f in *; do
	echo "====================== $f ========================"
	svnsync sync file://$(pwd)/$f
	svn up ../wcs/$f
done

echo "Done syncing!"
popd
echo -n - $(date) >> LEESMIJ.txt
read
