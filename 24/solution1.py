#!/usr/bin/python3
import numpy as np
import sys
import math


#example
data = """....#
#..#.
#..##
..#..
#...."""

# puzzle input
data = """#..#.
..#..
...##
...#.
#.###"""

maxX = 0
maxY = 1

seen = {}

for i in range(len(data)):
    maxX += 1

    if data[i] == '\n':
        maxY += 1
        maxX = 0

world = np.zeros((maxX, maxY), np.uint32)
i = 0
j = 0
for index in range(len(data)):
    if data[index] == '\n':
        j += 1
        i = 0
    else:
        world[i][j] = ord(data[index])
        i += 1
        
print(str(maxX) + " by " + str(maxY))
for j in range(maxY):
    print("")
    for i in range(maxX):
        sys.stdout.write(chr(world[i][j]))
print("")
while 1:
    world_copy = world.copy()
    for j in range(maxY):
        for i in range(maxX):
            neighbors = 0
            if i-1 >= 0 and world[i-1][j] == ord('#'):
                neighbors += 1
            if i+1 < maxX and world[i+1][j] == ord('#'):
                neighbors += 1
            if j-1 >= 0 and world[i][j-1] == ord('#'):
                neighbors += 1
            if j+1 < maxY and world[i][j+1] == ord('#'):
                neighbors += 1

            if world[i][j] == ord('#') and neighbors != 1:
                world_copy[i][j] = ord('.')
            elif world[i][j] == ord('.') and (neighbors == 1 or neighbors == 2):
                world_copy[i][j] = ord('#')

    world = world_copy
    """
    for j in range(maxY):
        print("")
        for i in range(maxX):
            sys.stdout.write(chr(world[i][j]))
    print("")
    """
    world_str = str(world)
    if world_str in seen:
        print("Seen")
        index = 0
        bio = 0
        for j in range(maxY):
            for i in range(maxX):
                if world[i][j] == ord('#'):
                    bio += math.pow(2, index)
                index += 1
        print("bio is " + str(bio))
        exit()
    seen[world_str] = 1
