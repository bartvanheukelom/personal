#!/bin/bash
set -e
cmd=${1:-st}

if [[ $cmd == "help" ]]; then
	echo "Usage: sgall.sh [cmd=st]"
	echo "Run the given command on all svn and git working copies in the current directory"
	exit 0
fi

# TODO allow specifying paths
# TODO recursive

echo "Doing $cmd on all repos"
for x in *; do
	if [[ -d $x ]]; then
		echo "$(tput setaf 2)$(tput bold)---------- ${x} ----------$(tput sgr0)"
		pushd $x > /dev/null
		if [[ -d ".svn" ]]; then
			echo "$(tput setaf 4)subversion$(tput sgr0)"
			echo
			svn $cmd 
		elif [[ -d ".git" ]]; then
			echo "$(tput setaf 5)git$(tput sgr0)"
			echo
			case $cmd in
				up)
					gcmd=pull
					;;
				st)
					gcmd=status
					;;
			esac
			git $gcmd
		else
			echo "Not a working copy"
		fi
		popd > /dev/null
		echo
		echo
	fi
done
