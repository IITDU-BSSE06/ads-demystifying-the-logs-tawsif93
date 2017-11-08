#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import date

# line = "10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] \"GET / HTTP/1.1\" 403 202"
for line in sys.stdin:
	data = line.strip().split('\"')
	data = data[1].strip().split(' ')
# data = data[0].strip().split('/')
# data = data[2].strip().split(':')
# if len(data) == 3:
# 	print data[1]
	print data[0]	

