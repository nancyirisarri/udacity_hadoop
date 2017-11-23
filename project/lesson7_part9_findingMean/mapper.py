#!/usr/bin/python
from datetime import datetime
import sys


# Find the mean value of sales on Sunday.
# Should output: 'Sunday': COUNT

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) == 6:
        # Get the weekday. Sunday is 6.
        weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()

        #if weekday == 6:        
            # Use weekday as output key
            #print("{0}\t".format(data[4]))
        print("{0}\t{1}".format(weekday, data[4]))
    