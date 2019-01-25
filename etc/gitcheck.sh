#!/bin/bash
set -e
cd ~
for g in $(find -type d -name .git); do
	pushd $(dirname $g)
	git status
	popd
done
