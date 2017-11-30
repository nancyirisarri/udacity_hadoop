#!/usr/bin/python
from decimal import Decimal, ROUND_HALF_UP
import sys


# Loop around the data
# In the mapper we looked for sales on Sunday and print the cost.

current_day = None
current_cost = 0
day = None

for line in sys.stdin:
    data = line.strip().split("\t")
    day, cost = data
    #print day, float(cost.replace("[", "").replace("]", "").replace("'", ""))
    
    # Something is wrong, cost cannot be float. Skip.
    try:
        cost = float(cost.replace("[", "").replace("]", "").replace("'", ""))
    except ValueError:
        continue

    if current_day == day:
        current_cost += cost
    else:
        if current_day:
            print("{0}\t{1}".format(current_day, current_cost))
        current_day = day
        current_cost = cost
        
#if current_day == day:        
    #print(
     #   "Total sales on ", "{0}: ".format(current_day), 
      #  str(Decimal(str(current_cost)).quantize(Decimal('1.11'), rounding=ROUND_HALF_UP))
       # )
