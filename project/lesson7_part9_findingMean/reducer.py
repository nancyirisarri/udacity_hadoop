#!/usr/bin/python
from decimal import Decimal, ROUND_HALF_UP
import sys


# Loop around the data
# In the mapper we looked for sales on Sunday and print the cost.

count = 0
sales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    # Something has gone wrong. Skip this line.
    if len(data_mapped) == 0:
        continue
    
    # Something is wrong, strings cannot be float. Skip.
    try:
        day = float(data_mapped[0])
        cost = float(data_mapped[1])
    except ValueError:
        continue
        
    if day == 6:
        count += 1
        sales += cost
    
print(
    'Mean of sales on Sunday: ', 
    str(Decimal(str(sales/count)).quantize(Decimal('1.11'), rounding=ROUND_HALF_UP))
    )
