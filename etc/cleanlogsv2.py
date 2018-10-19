#!/usr/bin/env python

# Compress, then delete, files in dated folders.
# Python 2

import sys
import datetime
import os
import subprocess

argv = sys.argv
argc = len(argv)

baseDir = argv[1]
ageCompress = int(argv[2]) if argc >= 3 else 1
ageDelete = int(argv[3]) if argc >= 4 else 7 
ageMax = int(argv[4]) if argc >= 5 else 30
print "ageCompress: " + str(ageCompress) + ", ageDelete: " + str(ageDelete) + ", ageMax: " + str(ageMax)

today = datetime.date.today()

os.chdir(baseDir)
baseDirAbs = os.getcwd()

for age in range(ageCompress, ageMax):
	os.chdir(baseDirAbs)
	date = today - datetime.timedelta(days=age)
	daydirname = str(date)
        
	if not os.path.isdir(daydirname):
		continue

	if age >= ageDelete:
		print "Delete " + daydirname
		os.system("rm -r " + daydirname)
	else:
		print "Compress " + daydirname
		subprocess.call(["find", "-name", "*.log", "-exec", "gzip", "{}", ";"], cwd=daydirname)
