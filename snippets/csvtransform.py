#!/usr/bin/env python3

import csv
import sys

inf = sys.stdin
#inf = open('infile.csv', 'r')
ouf = sys.stdout
#ouf = open('outfile.out', 'w')

r = csv.reader(inf)

for row in r:
	line = 'update table set foo = "' + row[1] + '" where bar = "' + row[0] + '";'
	ouf.write(line + '\n')

