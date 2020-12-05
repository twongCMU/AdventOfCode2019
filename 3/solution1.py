#!/usr/bin/python3

import numpy as np
import sys

startX = 11500
startY = 11500

start_sizeX = startX*2
start_sizeY = startY*2

np.set_printoptions(threshold=sys.maxsize)
# each array index contains an array of movement commands for that wire
wire_data = []

# each array index contains a dict of (x,y) points for that wire
wire_points = []

def print_matrix(matrix):
    for y in range(start_sizeY):
        print("")
        for x in range(start_sizeX):
            sys.stdout.write(str(matrix[x][y]))

# returns an array of points
def matrix_overlap(matrix_list, wire_points_list):
    num_wires = len(matrix_list)
    ret = []
    for point in wire_points_list:
        (x,y) = point
        count = 0
        for matrix in matrix_list:
            if matrix[x][y] > 0:
                count += 1
            else:
                break
        if count == num_wires:
            ret.append((x,y))
    return ret
                    

def walk(wire, overlap_point):
    wire_points_list = []
    coordX = startX
    coordY = startY

    steps = 0
    
    points = np.zeros((start_sizeX, start_sizeY), dtype=np.uint32)
    for move in wire:
        direction = move[0]
        count = int(move[1:])

        changeX = 0
        changeY = 0

        if direction == 'R':
            changeX = 1
        elif direction == 'U':
            changeY = 1
        elif direction == 'L':
            changeX = -1
        elif direction == 'D':
            changeY = -1
        else:
            print("UNKNOWN DIRECTION " + direction)
            exit()
            
        for i in range(count):
            steps += 1
            coordX += changeX
            coordY += changeY
            points[coordX][coordY] = 1

            wire_points_list.append((coordX, coordY))

            if overlap_point is not None:
                (overlapX, overlapY) = overlap_point
                if overlapX == coordX and overlapY == coordY:
                    return(None, None, steps)
            
    print("done")
    #print_matrix(points)
    return(points, wire_points_list, steps)


    

    
with open("input") as f:
    a = f.readline()
    while a:
        wire_data.append(a.strip().split(','))
        a = f.readline()

    f.close()

# test cases
#wire_data[0] = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#wire_data[1] = ['U62','R66','U55','R34','D71','R55','D58','R83']

#wire_data[0] = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
#wire_data[1] = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

# wire is one array of moves for a given wire

# a list of points for any wire
wire_points_list = []

for wire in wire_data:
    (points, wire_points_list, ignore) = walk(wire, None)
    wire_points.append(points)

overlap_points = matrix_overlap(wire_points, wire_points_list)
print(overlap_points)

min_distance = sys.maxsize
for overlap in overlap_points:
    (overlapX, overlapY) = overlap

    distance = abs(overlapX - startX) + abs(overlapY - startY)
    print("Distance for " + str(overlap) + " was " + str(distance))

    if distance < min_distance:
        min_distance = distance

print("Min distance: " + str(min_distance))

min_steps = sys.maxsize
for overlap in overlap_points:
    step_count = 0
    for wire in wire_data:
        (ignore, ignore2, steps) = walk(wire, overlap)
        step_count += steps
    print("For point " + str(overlap) + " steps were " + str(step_count))
    if step_count < min_steps:
        min_steps = step_count
print("min steps: " + str(min_steps))
