#!/usr/bin/env python3

import csv
import sys

inf = sys.stdin
#inf = open('infile.csv', 'r', encoding="utf-8")
ouf = sys.stdout
#ouf = open('outfile.out', 'w', encoding="utf-8")

r = csv.reader(inf)
w = csv.writer(ouf)

for row in r:
	#line = 'update table set foo = "' + row[1] + '" where bar = "' + row[0] + '";'
	#ouf.write(line + '\n')
	w.writerow(row)
