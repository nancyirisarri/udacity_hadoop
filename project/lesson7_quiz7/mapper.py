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

"""
# Trying to clean up the lines, since in the file there are blank lines and
# lines split into multiple lines.
isNewline = True

#reader = csv.reader(sys.stdin, delimiter='\t')

#while isNewline == True:
for line in sys.stdin:
#for line in reader:
    #currline = None
    
    # needed for first iteration
    #if currline is None:
    currline = line#sys.stdin.next()#sys.stdin.readline()#line
        #currline = lines[i]
    
    # break from the while
    #if not currline: 
        #break

    nextline = ''
    nextline_split = []
    #try:
        #nextline = sys.stdin.next()#next(fb)
        #nextline_split = nextline.split()
    #except StopIteration:
        #pass
    
    # get next line, skipping blank lines            
    while isNewline == True and len(nextline_split) == 0:
        try:
            nextline = sys.stdin.next()#next(fb)
            nextline_split = nextline.split()
        except StopIteration:
            # TODO split, regex, print, break?
            currline = currline.replace("\r\n", "\n").replace("\n", "")
            data = re.split(regex, currline)
            print '\t'.join(data)
            isNewline = False
        
    # remove empty items
    #nextline_split = [j for j in nextline_split if len(j) > 0]

    # remove quotes and keep id
    nextline_id = nextline_split[0].replace('"', "")
    
    # get next lines that do not begin with digit
    while isNewline == True and nextline_id.isdigit() == False:
        currline += " " + nextline
        
        try:
            nextline = sys.stdin.next()#next(fb)
            nextline_split = nextline.split()
        except StopIteration:
            currline = currline.replace("\r\n", "\n").replace("\n", "")
            data = re.split(regex, currline)
            print '\t'.join(data)
            isNewline = False
        
        # skip blank lines            
        while isNewline == True and len(nextline_split) == 0:
            try:
                nextline = sys.stdin.next()#next(fb)
                nextline_split = nextline.split()
            except StopIteration:
                currline = currline.replace("\r\n", "\n").replace("\n", "")
                data = re.split(regex, currline)
                print '\t'.join(data)
                isNewline = False
        
        nextline_id = nextline_split[0].replace('"', "")
        nextline_split = [j for j in nextline_split if len(j) > 0]
        
    currline = currline.replace("\r\n", "\n").replace("\n", "")
    
    data = re.split(regex, currline)
    
    print '\t'.join(data)

    if isNewline == False:
        break    
    #currline = nextline
    #currline = ""
"""