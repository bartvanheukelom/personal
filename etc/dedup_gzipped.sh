#!/bin/bash
# https://github.com/bartvanheukelom
set -e

# TODO don't remove, but print dupe files to stdout to be passed into e.g. xargs

if [[ "$1" == "" || "$1" == "-h" || "$1" == "--help" ]]; then
		echo "Usage: dedup_gzipped.sh DIR [dry]"
		echo
		echo "Recursively scan DIR for gzipped files, then for each"
		echo "gz file, if a file with the same name but uncompressed"
		echo "exists, check if the contents are the same, and if so"
		echo "delete the uncompressed file."
		echo
		echo "Pass 'dry' as second argument to only display what is"
		echo "going to be deleted without actually doing so"
		exit 1
fi

cd "$1"
echo "Checking zip duplicates in $(pwd)"

find -name \*.gz -print0 | while read -d '' -r zipped; do
		unzipped="${zipped%???}"
		if [[ -f "$unzipped" ]]; then
				echo -n "$unzipped..."
				# TODO mktemp
				tmp="$zipped.tmp_unzipped_for_cmp"
				gzip --decompress --stdout "$zipped" > "$tmp"
				if cmp --silent "$unzipped" "$tmp"; then
						echo " -> Delete"
						if [[ "$2" != "dry" ]]; then
								rm "$unzipped"
						fi
				else
						echo " -> WARN: contents do not match"
				fi
				rm "$tmp"
		fi
done
