#!/usr/bin/python3


import numpy as np
import sys
import math
import os

"""
looped 1000 times
looped 2000 times
looped 3000 times
looped 4000 times
looped 5000 times
looped 6000 times
looped 7000 times
looped 8000 times
looped 9000 times
looped 10000 times
repeat at 10006 last seen at 0
repeat at 10007 last seen at 1
repeat at 10008 last seen at 2
repeat at 10009 last seen at 3
repeat at 10010 last seen at 4
repeat at 10011 last seen at 5
repeat at 10012 last seen at 6
repeat at 10013 last seen at 7
repeat at 10014 last seen at 8
repeat at 10015 last seen at 9
"""

f = open("input", 'r')
lines = f.readlines()

position = 2020

for line_data in lines:
    line = line_data.strip()

    if len(line) < 3:
        continue
    
    if line == "deal into new stack":
        position *= -1
        
    elif line[:3] == "cut":
        (ignore, cut_number) = line.split(' ')
        cut_number = int(cut_number)

        position -= cut_number

    elif line[:9] == "deal with":
        deal_number = int(line[len("deal with increment "):])

        #### relvelation: deal_number is always small. So, slot 2020 never wraps around
    else:
        print("UNKNOWN LINE " + line)
        exit()

    for i, v in enumerate(deck):
        if v == 2020:
            print("card 2020 is in position " + str(i))

for i, v in enumerate(deck):
    """ # part 1
    if v == 2019:
        print("card 2019 is in position " + str(i))
    """
