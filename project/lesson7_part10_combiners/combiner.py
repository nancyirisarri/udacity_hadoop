#!/usr/bin/python
from datetime import datetime
import sys

sales_dic = dict()

for line in sys.stdin:
    #sales_dic = dict()

    data = line.strip().split("\t")
    
    # Something has gone wrong. Skip this line.
    #if len(data) == 0:
    #if len(data) != 6:
        #continue

    #day, cost = data
    day = datetime.strptime(data[0], "%Y-%m-%d").weekday()
    cost = data[4]
    #print day, cost

    if day not in sales_dic.keys():
        sales_dic[day] = [cost]
    else:
        sales_dic[day].append(cost)
    
for d in sales_dic.keys():
    print("%s\t%s" % (d, sales_dic[d]))
