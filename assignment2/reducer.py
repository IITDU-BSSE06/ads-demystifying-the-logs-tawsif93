#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	mapped = line.strip().split(" ")
	if mapped[1]=="/assets/js/the-associates.js":
		salesTotal+=1

	# print thisKey, "\t", thisSale
  #  if oldKey and oldKey != thisKey:
   #	 print oldKey, "\t", salesTotal
	#	oldKey = thisKey;
	 #   salesTotal = 0
#
 #   oldKey = thisKey
  #  salesTotal += float(thisSale)

#if oldKey != None:
print salesTotal

