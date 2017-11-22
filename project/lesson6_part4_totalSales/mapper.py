#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want element 4 (cost)
# We need to write it out to standard output, separated by a tab

import sys

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t".format(cost)

