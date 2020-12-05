#!/usr/bin/python3

import numpy as np
import math 


data_string = """....
.###
...."""


data_string = """.#..#
.....
#####
....#
...##"""



# test 1 best is 5,8 with 33
data_string = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""


# my data, best is #11, 19 with 253
data_string = """#..#.#.#.######..#.#...##
##.#..#.#..##.#..######.#
.#.##.#..##..#.#.####.#..
.#..##.#.#..#.#...#...#.#
#...###.##.##..##...#..#.
##..#.#.#.###...#.##..#.#
###.###.#.##.##....#####.
.#####.#.#...#..#####..#.
.#.##...#.#...#####.##...
######.#..##.#..#.#.#....
###.##.#######....##.#..#
.####.##..#.##.#.#.##...#
##...##.######..##..#.###
...###...#..#...#.###..#.
.#####...##..#..#####.###
.#####..#.#######.###.##.
#...###.####.##.##.#.##.#
.#.#.#.#.#.##.#..#.#..###
##.#.####.###....###..##.
#..##.#....#..#..#.#..#.#
##..#..#...#..##..####..#
....#.....##..#.##.#...##
.##..#.#..##..##.#..##..#
.##..#####....#####.#.#.#
#..#..#..##...#..#.#.#.##"""


sizeX = 0
sizeY = 1
for a in data_string:
    if a is not '\n':
        sizeX += 1
    else:
        sizeX = 0
        sizeY += 1
        
print("Dim is " + str(sizeX) + " by " + str(sizeY))

data = np.zeros(sizeY*sizeX, np.uint32)

offset = 0
for a in data_string:
    if a == '#':
        data[offset] = 1
        offset += 1
    elif a == '.':
        data[offset] = 0
        offset += 1

data = np.reshape(data, (sizeY, sizeX))
print(str(data))
# returns a list of relative x,y changes from the current point for a distance away
def make_distance(distance):
    changeX = range(distance * -1, distance + 1)
    changeY = range(distance * -1, distance + 1)
    change_list = []
    
    for x in [distance, -1 * distance]:
        for y in changeY:
            if x == 0 and y == 0:
                continue
            change_list.append((x,y))

    for x in changeX:
        for y in [distance, -1 * distance]:

            if x == 0 and y == 0:
                continue
            change_list.append((x,y))

    temp_dict = {}
    for a in change_list:
        temp_dict[a] = 1
        
    return list(temp_dict.keys())

# returns None if distance is too big
def search_from(pointX, pointY, seen_list, distance, data):
    check_list = make_distance(distance)

    new_seen_list = []
    # if we didn't see any valid points then distance is high enough that every point is off the map
    had_good = False
    for c in check_list:
        (checkX, checkY) = c

        is_blocked = False
        for seen in seen_list:
            seen_base = seen
            (seen_baseX, seen_baseY) = seen_base
            gcd = math.gcd(seen_baseX, seen_baseY)
            if gcd > 1:
                seen_base = (seen_baseX/gcd, seen_baseY/gcd)
                
            multiplier = 2
            while multiplier < 25:
                (seenX, seenY) = seen_base
                seenX *= multiplier
                seenY *= multiplier

                if seenX == checkX and seenY == checkY:
                    is_blocked = True
                    break

                absoluteX = pointX + seenX
                absoluteY = pointY + seenY

                # if it is off the end of the grid, skip
                if absoluteX < 0 or absoluteY < 0 or absoluteX >= sizeX or absoluteY >= sizeY:
                    break
                
                multiplier += 1
                
            if is_blocked:
                break
            
        if is_blocked:
            continue
            
        
        absoluteX = pointX + checkX
        absoluteY = pointY + checkY

        # if it is off the end of the grid, skip
        if absoluteX < 0 or absoluteY < 0 or absoluteX >= sizeX or absoluteY >= sizeY:
            continue
        
    
        had_good = True

        if data[absoluteY][absoluteX] > 0:
            new_seen_list.append(c)


    if not had_good:
        return None
    
    seen_list.extend(new_seen_list)
    return seen_list

highest = 0
highestX = 0
highestY = 0
for tryX in range(sizeX):
    for tryY in range(sizeY):
        if data[tryY][tryX] > 0:
            seen_list = []
            distance = 1
            while distance < 200:
                new_seen_list = search_from(tryX,tryY, seen_list, distance, data)
                if new_seen_list is None:
                    break

                seen_list = new_seen_list
                distance += 1

            if len(seen_list) > highest:
                highest = len(seen_list)
                highestX = tryX
                highestY = tryY
            print("Seen list for " + str(tryX) + "," + str(tryY) + " with items: " + str(len(seen_list)))
        
print("highest was " + str(highest) + " " +str(highestX) + " " + str(highestY))
