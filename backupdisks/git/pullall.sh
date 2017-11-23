#!/bin/bash

# Run git pull on all clone dirs

set -e

for d in *; do
	if [ -d "$d" ]; then
		echo ">> git pull $d"
		pushd $d
		git pull
		popd
	fi
done

echo "All pulled!"
read
