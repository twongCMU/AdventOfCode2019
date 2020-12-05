#!/usr/bin/python3

import numpy as np
import sys

f = open("input_test", 'r')

lines = f.readlines()

sizeX = len(lines[0])
sizeY = len(lines)

world = np.zeros((sizeX, sizeY), np.uint32)

robotX = 0
robotY = 0


keys = []
for j, line in enumerate(lines):
    for i, character in enumerate(line.strip()):
        if character == '@':
            robotX = i
            robotY = j

        if character.islower():
            keys.append(character)

            
            
        world[i][j] = ord(character)

num_keys = len(keys)

MAX_UINT32 = 4294967295
def print_world():
    for j, line in enumerate(lines):
        print("")
        for i, character in enumerate(line):
            sys.stdout.write(chr(world[i][j]))

def search_world(curX_in, curY_in, key_list_in, prevX_in, prevY_in):
    pending = []

    results = []
    min_result = MAX_UINT32
    search_depth = 0
    pending.append((curX_in, curY_in, key_list_in, prevX_in, prevY_in, search_depth))
    count = 0

    longest_depth = 0
    while len(pending) > 0:
        count += 1
        if count%100000==0:
            best = ""
            if len(results) > 0:
                best = str(min(results))
            print("count " + str(count) + " queue depth " + str(len(pending)) + " best result " + best + " deepest " + str(longest_depth))
        (curX, curY, key_list, prevX, prevY, search_depth) = pending.pop(0)

        if search_depth > min_result:
            continue
        
        if search_depth > longest_depth:
            longest_depth = search_depth
        found_key = False
        #print("have " + str(len(key_list)) + " keys at " + str(curX) + " " + str(curY))
        current_tile = chr(world[curX][curY])

        # if we are at a lock and we don't have the key, we're done
        if current_tile.isupper() and current_tile.lower() not in key_list:
            print("at a lock without the key. dying")
            continue

        # if we are on a key tile and we already have the key, this is not an optimal
        # path so we return right away
        #if current_tile.islower() and current_tile in key_list:
        #    return MAX_UINT32

        # if we are on a key tile and we don't have the key, pick it up
        if current_tile.islower() and current_tile not in key_list:
            key_list.append(current_tile)
            found_key = True
            if len(key_list) == num_keys:
                if search_depth < min_result:
                    min_result = search_depth
                results.append(search_depth)
                #print("adding solution at " + str(search_depth))
                continue

        # recurse in all directions except the one we came from
        lowest_path = MAX_UINT32
        if curX + 1 < sizeX and (found_key is True or prevX != curX + 1) and world[curX+1][curY] != ord('#'):
            print("at " + str(curX) + " " + str(curY) + " moving right depth " + str(search_depth+1) + " keys " + str(key_list))
            pending.append((curX + 1, curY, key_list.copy(), curX, curY, search_depth+1))
        if curX - 1 >= 0 and (found_key is True or prevX != curX - 1) and world[curX-1][curY] != ord('#'):
            print("at " + str(curX) + " " + str(curY) + " moving left depth " + str(search_depth+1) + " keys " + str(key_list))
            pending.append((curX - 1, curY, key_list.copy(), curX, curY, search_depth+1))
        if curY + 1 < sizeY and (found_key is True or prevY != curY + 1) and world[curX][curY+1] != ord('#'):
            print("at " + str(curX) + " " + str(curY) + " moving down depth " + str(search_depth+1) + " keys " + str(key_list))
            pending.append((curX, curY + 1, key_list.copy(), curX, curY, search_depth+1))
        if curY - 1 >= 0 and (found_key is True or prevY != curY - 1) and world[curX][curY-1] != ord('#'):
            print("at " + str(curX) + " " + str(curY) + " moving up depth " + str(search_depth+1) + " keys " + str(key_list))
            pending.append((curX, curY - 1, key_list.copy(), curX, curY, search_depth + 1))


    #print("results: " + str(results))
    print("min : " + str(min(results)))

        


print_world()
print(str(search_world(robotX, robotY, [], robotX, robotY)))



