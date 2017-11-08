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

C2009 = 0
C2010 = 0
C2011 = 0

# line = "2009"
for line in sys.stdin:
	mapped = line.strip()
	if mapped == "2009":
		C2009+=1
	if mapped == "2010":
		C2010+=1
	if mapped == "2011":
		C2011+=1
	# print thisKey, "\t", thisSale
  #  if oldKey and oldKey != thisKey:
   #	 print oldKey, "\t", salesTotal
	#	oldKey = thisKey;
	 #   salesTotal = 0
#
 #   oldKey = thisKey
  #  salesTotal += float(thisSale)

#if oldKey != None:
print "2009 " + str(C2009) + "\n" + "2010 " + str(C2010) + "\n" + "2011 " + str(C2011) + "\n"
print C2009
print C2010
print C2011

