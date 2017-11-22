#!/usr/bin/python

# Make index of words and node id for body of forum post.
# Split the text on all: whitespace, ., ,, !, ?, :, ;, ", (, ), <, >, [, ], #, $, =, -, /
# Then 1) count word fantastic, case insensitive; 2) list nodes in ascending order
# which contain fantastically.

import re
import sys


regex = '[\s|\.|,|!|\?|:|;|"|\(|\)|<|>|\[|\]|#|\$|=|-|\/]+'

# As per the instructions, split the body on given characters.
for line in sys.stdin:
    data = re.split(regex, line)
    print('\t'.join(data))