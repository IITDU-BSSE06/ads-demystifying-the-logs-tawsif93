#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
	data = line.strip().split("- -")
	if len(data) == 2:
		ip, value = data
		print "{0}\t{1}".format(ip, value)

