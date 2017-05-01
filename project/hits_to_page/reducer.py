#!/usr/bin/python

import sys

count = 0

# Loop around the data
# Since we used a regex and evaluated the request, here only count 
# the results from the mapper.

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    if data_mapped[0] != '/assets/js/the-associates.js':
        # Make sure we are counting the page in question. If not, skip this line.
        continue

    count += 1
    
print '/assets/js/the-associates.js', "\t", count

