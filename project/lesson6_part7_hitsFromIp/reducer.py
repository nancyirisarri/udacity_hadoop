#!/usr/bin/python
import sys


# Loop around the data
# Since we used a regex and evaluated the request, here only count 
# the results from the mapper.

count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    if data_mapped[0] != '10.99.99.186':
        # Make sure we are counting the IP in question. If not, skip this line.
        continue

    count += 1
    
print('10.99.99.186', "\t", count)
