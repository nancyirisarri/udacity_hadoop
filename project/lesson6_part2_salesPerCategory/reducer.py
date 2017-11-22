#!/usr/bin/python

import sys

itemsTotal = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the item description, val is the sale amount
#
# All the costs for a particular item will be presented,
# If it is in the map, add the sale amount to the value,
# else add a new key/value pair to the dictionary.

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    
    if thisKey in itemsTotal:
        itemsTotal[thisKey] += float(thisSale)
    else:
        itemsTotal[thisKey] = float(thisSale)

for key, value in itemsTotal.iteritems():
    print key, "\t", value

