#!/usr/bin/python3

import numpy as np
import math 


# 8,1  9,0  9,1  10,0  9,2  11,1  12,1  11,2  15,1
# 12,2  13,2  14,2  15,2  12,3  16,4  15,4  10,4  4,4
# 2,4  2,3  0,2  1,2  0,1  1,1  5,2  1,0  5,1
# 6,1  6,0  7,0
# R2: 8,0  10,1  14,0  16,1  13,3
# R3: 14,3
data_string = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##"""

bestX = 8
bestY = 3


data_string = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

bestX = 11
bestY = 13

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

bestX = 11
bestY = 19

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
num_asteroids = 0
offset = 0
for a in data_string:
    if a == '#':
        data[offset] = 1
        num_asteroids += 1
        offset += 1
    elif a == '.':
        data[offset] = 0
        offset += 1
print("Num asteroids = " + str(num_asteroids))
data = np.reshape(data, (sizeY, sizeX))
data[bestY][bestX] = 5
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

# highest for my solution is at 24, 24 for 253

astroids_vaporized = 0
rounds = 1
while astroids_vaporized < (num_asteroids-1): # -1 since we don't count the one with the station on it
    print("round " + str(rounds))
    rounds += 1
    
    seen_list = []
    distance = 1
    while distance < 50:
        new_seen_list = search_from(bestX,bestY, seen_list, distance, data)
        if new_seen_list is None:
            break

        seen_list = new_seen_list
        distance += 1

    print("Seen list for " + str(bestX) + "," + str(bestY) + " with items: " + str(len(seen_list)))
    print("Seen list is " + str(seen_list))

    seen_dict = {}
    for a in seen_list: # seen_list is relative to current position so +  is down and right not up and right
        (seenX, seenY) = a
        if seenX == 0 and seenY > 0:
            deg = 180
        elif seenX == 0 and seenY < 0:
            deg = 0
        elif seenX > 0 and seenY == 0:
            deg = 90
        elif seenX < 0 and seenY == 0:
            deg = 270
        else:
            if seenX > 0 and seenY > 0:
                deg = abs(np.degrees(math.atan((seenY * 1.0)/(seenX* 1.0))))
                deg += 90
            elif seenX < 0 and seenY < 0:
                deg = abs(np.degrees(math.atan((seenY * 1.0)/(seenX* 1.0))))
                deg += 270
            elif seenX < 0 and seenY > 0:
                deg = abs(np.degrees(math.atan((seenX * 1.0)/(seenY* 1.0))))
                deg += 180
            else:
                deg = abs(np.degrees(math.atan((seenX * 1.0)/(seenY* 1.0))))

        seen_dict[deg] = a

    seen_keys = sorted(seen_dict.keys())
    for a in seen_keys:
        print(str(a) + " " + str(seen_dict[a]))
    for asteroid in sorted(seen_dict.keys()):
        (relativeX, relativeY) = seen_dict[asteroid]
        absoluteX = bestX + relativeX
        absoluteY = bestY + relativeY

        data[absoluteY][absoluteX] = 0
        #print(str(data))
        astroids_vaporized += 1

        print("asteroid " + str(astroids_vaporized) + " " + str(absoluteX) + " " + str(absoluteY))
        if astroids_vaporized == 200:
            print("200th was " + str(absoluteX) + " " + str(absoluteY))


    if rounds == 30:
        print("final " + str(data))
        exit()

