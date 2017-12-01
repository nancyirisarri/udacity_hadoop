#!/usr/bin/python
from datetime import datetime
import sys


# Find the sales for each day.

for line in sys.stdin:
    data = line.strip().split("\t")
    
    # Get the weekday Sunday is 6.
    weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
    cost = data[4]

    print("{0}\t{1}".format(weekday, cost))
