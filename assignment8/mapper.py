#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from urlparse import urlparse
# line = "10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] \"GET www.c.com/images/filmmediablock/360/GOEMON-NUKI-000159.jpg HTTP/1.1\" 403 202"

for line in sys.stdin:
	data = line.strip().split('"')
	if len(data) == 3:
		mapped= data[1].strip().split(" ")
		path = urlparse(mapped[1]).path
		print path
		# file = path.split("/")
		# file = file[len(file)-1].strip()
		# print file

