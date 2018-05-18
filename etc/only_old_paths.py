#!/usr/bin/env python3

import sys
import os
import datetime

def is_old_date(date, age):
		try:
				fdate = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
				return (datetime.date.today() - fdate).days >= age
		except:
				return False

def is_old_path(path, age):
		parts = path.split('/')
		return parts and is_old_date(parts[-1], age)


# main #

try:
		age=int(sys.argv[1])
except IndexError:
		print("Usage: only_old_paths.py DAYS_AGE")
		print("Given a list of paths on STDIN, output those whose")
		print("basename is an ISO date (YYYY-MM-DD) that is at least")
		print("DAYS_AGE days ago.")
		sys.exit(1)

for line_in in sys.stdin:
		if is_old_path(line_in.strip(), age):
				print(line_in, end="")
