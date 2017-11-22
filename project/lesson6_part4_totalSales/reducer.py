#!/usr/bin/python
import sys


# Loop around the data
# It will be in the format val\t
# Where val is the sale amount
#
# All the sales for a particular store will be presented.
# For each a counter will be increased and the value of the
# sale amount added to a variable.

salesCount = 0
salesValue = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisSale = data_mapped[0]

    salesCount += 1
    salesValue += float(thisSale)

print(salesCount, "\t", salesValue)
