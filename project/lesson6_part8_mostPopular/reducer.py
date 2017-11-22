#!/usr/bin/python

import sys

maximum = 0
popPage = None
pages = {}

# Loop around the data
# It will be in the format page\t
# Where page is the path of the request.
#
# If the page is not in the dictionary, add a new key/value
# pair to the dictionary; else increase the value for the page.
# Then, if the maximum is less than the count for this page,
# update the maximum and the variable with the most popular page.

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]
    
    if thisKey not in pages:
        pages[thisKey] = 1
    else:
        pages[thisKey] += 1

    if maximum < pages[thisKey]:
        maximum = pages[thisKey]
        popPage = thisKey

print popPage, "\t", maximum
