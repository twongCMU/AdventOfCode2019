#!/usr/bin/python3


import numpy as np
import sys
import math
import os

f = open("input", 'r')
lines = f.readlines()

cards = 10007
deck = []
for i in range(cards):
    deck.append(i)

seen = {}
main_loop = 0
while 1:
    for line_data in lines:
        line = line_data.strip()

        if len(line) < 3:
            continue

        if line == "deal into new stack":
            deck.reverse()
        elif line[:3] == "cut":
            (ignore, cut_number) = line.split(' ')
            cut_number = int(cut_number)
            cut_start = deck[:cut_number]
            cut_end = deck[cut_number:]

            deck = cut_end
            deck.extend(cut_start)

        elif line[:9] == "deal with":
            deal_number = int(line[len("deal with increment "):])
            new_deck = [0]*cards
            index = 0

            rounds = 0
            firsts = [0]
            for v in deck:
                new_deck[index] = v
                index += deal_number

                if index >= cards:
                    rounds+=1
                    firsts.append(index%cards)
                index = index % cards
            #print("firsts " + str(firsts))
            deck = new_deck
            #print("Deal number " + str(deal_number) + " with rounds " + str(rounds))

        else:
            print("UNKNOWN LINE " + line)
            exit()

    if deck[2020] in seen:
        print("repeat at " + str(main_loop) + " last seen at " + str(seen[deck[2020]]))
    seen[deck[2020]] = main_loop

    main_loop += 1
    if main_loop % 1000 == 0:
        print("looped " + str(main_loop) + " times")
#for i, v in enumerate(deck):
    """ # part 1
    if v == 2019:
        print("card 2019 is in position " + str(i))
    """
