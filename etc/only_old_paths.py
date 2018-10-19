#!/usr/bin/env python3
# See below for documentation

import sys
import os
import datetime
import re

date_pattern = re.compile('(\d{4})-(\d{2})-(\d{2})', re.ASCII)

def is_old_date(datestr, age):
	m = date_pattern.fullmatch(datestr)
	if m:
		fdate = datetime.date(*[int(p) for p in m.group(1,2,3)])
		return (datetime.date.today() - fdate).days >= age
	else:
		return False

def is_old_path(path, age):
		parts = path.split('/')
		return parts and is_old_date(parts[-1], age)


if __name__ == "__main__":

	try:
			age=int(sys.argv[1])
	except IndexError:
			print("Usage: only_old_paths.py DAYS_AGE")
			print("Given a list of paths on STDIN, output those whose")
			print("basename is an ISO date (YYYY-MM-DD) that is at least")
			print("DAYS_AGE days ago.")
			print()
			print("Example:")
			print("  find /logs -type d | only_old_paths.py 2 | xargs rm -r")
			sys.exit(1)

	for line_in in sys.stdin:
			if is_old_path(line_in.strip(), age):
					print(line_in, end="")
		