#!/usr/bin/python

import sys

itemsTotal = {}
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the costs for a particular item will be presented,
# then the key will change and we'll be dealing with the next item

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        oldKey = thisKey;

    oldKey = thisKey
    
    if thisKey in itemsTotal:
        itemsTotal[thisKey] += float(thisSale)
    else:
        itemsTotal[thisKey] = float(thisSale)

if oldKey != None:
    for key, value in itemsTotal.iteritems():
        print key, "\t", value

