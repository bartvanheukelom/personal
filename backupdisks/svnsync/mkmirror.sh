#!/bin/bash

if [ "$1" == "" ]; then
	echo "Usage: mkmirror.sh NAME URL"
	exit 1
fi

name=$1
src=$2

echo "Create repo $name"
svnadmin create repos/$name

echo "Allo prop change"
cp pre-revprop-change repos/$name/hooks/
chmod +x repos/$name/hooks/pre-revprop-change

echo "Init svnsync"
svnsync initialize file://$(pwd)/repos/$name $src
svn co file://$(pwd)/repos/$name wcs/$name
