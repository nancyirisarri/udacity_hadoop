#!/usr/bin/python

# Format of each line is according to the Common Log Format
# %h %l %u %t \"%r\" %>s %b
#
# We want element %h, the IP address,
# and only when equal to the IP in question.
# We need to write it out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    regex = '([(\d\.)]+) ([^\s]+) ([^\s]+) \[(.*?)\] "(.*?)" (\d+) (\d+|-)'

    if re.match(regex, line) is not None:
        data = re.match(regex, line).groups()

        if len(data) == 7 and data[0] == '10.99.99.186':
            print "{0}\t".format(data[0])

