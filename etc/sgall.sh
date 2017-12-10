#!/bin/bash
set -e
cmd=${1:-st}

if [[ $cmd == "help" ]]; then
	echo "Usage: sgall.sh [cmd=st]"
	echo "Run the given command on all svn and git working copies in the current directory"
	exit 0
fi

echo "Doing $cmd on all repos"
for x in *; do
	if [[ -d $x ]]; then
		pushd $x
		if [[ -d ".svn" ]]; then
			svn $cmd 
		elif [[ -d ".git" ]]; then
			case $cmd in
				up)
					gcmd=pull
					;;
				st)
					gcmd=status
					;;
			esac
			git $gcmd
		fi
		popd
	fi
done
