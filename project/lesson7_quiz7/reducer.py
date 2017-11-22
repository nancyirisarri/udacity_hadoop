#!/usr/bin/python

# Loop around the data
# In the mapper we used a regex and split the body. Here we look
# and count for the words fantastic and fantastically.

import re
import sys


count = 0
ids = []
last_id = 0

p = re.compile(r'\bfantastic\b', re.IGNORECASE)

for line in sys.stdin:

    data_mapped = line.strip().split("\t")

    # Something has gone wrong. Skip this line.
    if len(data_mapped) == 0:
        continue

    # Keep a last id for lines that are split into several lines.
    node_id = data_mapped[0]
    if node_id.isdigit() == True:
        last_id = node_id

    # Count fantastic.
    fantastic = p.findall(line)
    count += len(fantastic)
    
    # Count fantastically, keeping the id that is a digit.
    fantastically = [i for i in data_mapped if 'fantastically' in i.lower()]
    
    if len(fantastically) > 0:
        if node_id.isdigit() == False:
            ids.append(int(last_id))
        else:
            ids.append(int(node_id))
    
print('fantastic was used: ', count)
print('fantastically is in nodes: ', sorted(ids))