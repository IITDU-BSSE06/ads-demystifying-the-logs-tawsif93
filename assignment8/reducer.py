#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

maxFile = None
maxCount = 0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	thisKey = line.strip()

	if oldKey and oldKey != thisKey:
#	 print oldKey, "\t", salesTotal
		if maxCount < salesTotal:
			maxCount = salesTotal
			maxFile = oldKey
		oldKey = thisKey;
		salesTotal = 1

	oldKey = thisKey
	salesTotal += 1
if maxCount < salesTotal:
	maxCount = salesTotal
	maxFile = oldKey

print maxFile + " " + str(maxCount)
