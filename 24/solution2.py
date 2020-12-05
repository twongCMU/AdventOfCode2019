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


for i in range(len(data)):
    maxX += 1

    if data[i] == '\n':
        maxY += 1
        maxX = 0

worlds = {}
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

worlds[0] = world
worlds[1] = np.zeros((maxX, maxY), np.uint32)
for j in range(maxY):
    for i in range(maxX):
        worlds[1][i][j] = ord('.')
worlds[-1] = np.zeros((maxX, maxY), np.uint32)
for j in range(maxY):
    for i in range(maxX):
        worlds[-1][i][j] = ord('.')

                
# returns [(absolute level, absolute x, absolute y), ...]
def translate_coord(world, curX, curY, testX, testY):
    # cases on the edge where we go out one level
    if testX < 0: 
        return [(world-1, 1, 2)]
    if testX >= maxX: 
        return [(world-1, 3, 2)]
    if testY < 0: 
        return [(world-1, 2, 1)]
    if testY >= maxY:
        return [(world-1, 2, 3)]

    # cases in the center tile
    if curX == 1 and curY == 2 and testX == 2 and testY == 2: # left
        return [(world+1, 0, 0), (world+1, 0, 1), (world+1, 0, 2), (world+1, 0, 3), (world+1, 0, 4)]
    if curX == 2 and curY == 1 and testX == 2 and testY == 2: # up
        return [(world+1, 0, 0), (world+1, 1, 0), (world+1, 2, 0), (world+1, 3, 0), (world+1, 4, 0)]
    if curX == 3 and curY == 2 and testX == 2 and testY == 2: # right
        return [(world+1, 4, 0), (world+1, 4, 1), (world+1, 4, 2), (world+1, 4, 3), (world+1, 4, 4)]
    if curX == 2 and curY == 3 and testX == 2 and testY == 2: # down
        return [(world+1, 0, 4), (world+1, 1, 4), (world+1, 2, 4), (world+1, 3, 4), (world+1, 4, 4)]

    return [(world, testX, testY)]
for minute in range(200):
    print("minute " + str(minute))
    worlds_copy = {}
    for worlds_index in worlds.keys():
        worlds_copy[worlds_index] = worlds[worlds_index].copy()

    for world in worlds.keys():
        for j in range(maxY):
            for i in range(maxX):
                if i == 2 and j == 2:
                    continue
                coords = translate_coord(world, i,j,i-1,j)
                coords.extend(translate_coord(world, i,j,i+1,j))
                coords.extend(translate_coord(world, i,j,i,j+1))
                coords.extend(translate_coord(world, i,j,i,j-1))

                neighbors = 0                
                for c in coords:
                    (testW, testX, testY) = c

                    if testW in worlds:
                        if worlds[testW][testX][testY] == ord('#'):
                            neighbors += 1

                if worlds[world][i][j] == ord('#') and neighbors != 1:
                    worlds_copy[world][i][j] = ord('.')
                elif worlds[world][i][j] == ord('.') and (neighbors == 1 or neighbors == 2):
                    worlds_copy[world][i][j] = ord('#')


    world_keys = list(worlds.keys())
    world_max = max(world_keys)
    world_min = min(world_keys)

    make = False
    for j in [0,4]:
        for i in range(5):
            if worlds_copy[world_max][i][j] == ord('#'):
                make = True
                break
        if make:
            break
    for i in [0,4]:
        for i in range(5):
            if worlds_copy[world_max][i][j] == ord('#'):
                make = True
                break
        if make:
            break
    if make:
        worlds_copy[world_max + 1] = np.zeros((maxX, maxY), np.uint32)
        for j in range(maxY):
            for i in range(maxX):
                worlds_copy[world_max+1][i][j] = ord('.')


    make = False
    for j in [0,4]:
        for i in range(5):
            if worlds_copy[world_min][i][j] == ord('#'):
                make = True
                break
        if make:
            break
    for i in [0,4]:
        for j in range(5):
            if worlds_copy[world_min][i][j] == ord('#'):
                make = True
                break
        if make:
            break
    if make:
        worlds_copy[world_min - 1] = np.zeros((maxX, maxY), np.uint32)
        for j in range(maxY):
            for i in range(maxX):
                worlds_copy[world_min - 1][i][j] = ord('.')

            
    worlds = {}
    for worlds_copy_index in worlds_copy.keys():
        worlds[worlds_copy_index] = worlds_copy[worlds_copy_index].copy()

bugs = 0
for w in worlds:
    #print("World " + str(w))
    for j in range(maxY):
        #print("")
        for i in range(maxX):
            #sys.stdout.write(chr(worlds[w][i][j]))
            if chr(worlds[w][i][j]) == '#':
                bugs += 1
    #print("")

print("bugs " + str(bugs))

    
