#!/usr/bin/python

# Format of each line is according to the Common Log Format
# %h %l %u %t \"%r\" %>s %b
#
# We want element \"%r\" the request line from the client. 
# From the request we want the path, which is between the method and protocol,
# equal to the page in question.
# We need to write it out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    regex = '([(\d\.)]+) ([^\s]+) ([^\s]+) \[(.*?)\] "(.*?)" (\d+) (\d+|-)'

    if re.match(regex, line) is not None:
        data = re.match(regex, line).groups()

        if len(data) == 7 and data[4].split()[1] == '/assets/js/the-associates.js':
            print "{0}\t".format(data[4].split()[1])

