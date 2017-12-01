#!/usr/bin/python
import sys


# Loop around the data
# In the mapper we print the day and sales. Here add the sales and print.

sales_dic = dict()

for line in sys.stdin:
    data = line.strip().split("\t")
    weekday, cost = data
    cost = float(cost)

    if weekday not in sales_dic.keys():
        sales_dic[weekday] = cost
    else:
        sales_dic[weekday] += cost

for d in sorted(sales_dic.keys()):
    print("{0}\t{1}".format(d, sales_dic[d]))
