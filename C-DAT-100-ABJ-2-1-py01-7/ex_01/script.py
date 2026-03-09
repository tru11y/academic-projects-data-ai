#!/usr/bin/env python3

import sys
def count_char(arg):
    count=0
    try:
        for char in arg:
            for c in char:
                if  c.isalpha():
                    count+=1
        print (count)
        return 0
    except:
        sys.exit(84)

count_char(sys.argv[1:])
