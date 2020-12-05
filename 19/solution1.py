#!/usr/bin/python3

from intcode import intcode
import numpy as np
import sys
import math

data = [109,424,203,1,21102,11,1,0,1105,1,282,21101,18,0,0,1106,0,259,2101,0,1,221,203,1,21101,0,31,0,1105,1,282,21101,0,38,0,1106,0,259,21001,23,0,2,21202,1,1,3,21102,1,1,1,21102,57,1,0,1105,1,303,2101,0,1,222,21002,221,1,3,20101,0,221,2,21101,259,0,1,21101,0,80,0,1105,1,225,21102,198,1,2,21102,91,1,0,1106,0,303,1201,1,0,223,21002,222,1,4,21101,0,259,3,21102,225,1,2,21102,225,1,1,21102,1,118,0,1106,0,225,21001,222,0,3,21101,0,140,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1106,0,259,2101,0,1,223,21002,221,1,4,21002,222,1,3,21101,0,24,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,21001,23,0,1,21102,1,-1,3,21102,1,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,21202,-3,1,1,22101,0,-2,2,21202,-1,1,3,21102,1,250,0,1105,1,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21101,0,343,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21102,1,384,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0]

#data.extend([0]*1000)
            


sizeX = 2000
sizeY = 2000
target_square = 100

world = np.zeros((sizeX, sizeY), np.uint32)

curX = 0
curY = 0

maxX = sizeX
maxY = sizeY
count = 0

for j in range(maxY):
    for i in range(maxX):
        world[i][j] = 5

width = 1
start = 0
end_val = 5
for j in range(800, maxY):
    print("j is " + str(j))

    if start < 0:
        start = 0

    if end_val >= maxX:
        end_val = maxX-1
    seen = 0

    start_updated = False

    for i in range(start, end_val+1):
        computer = intcode(data.copy(), True)
        input_args = [i, j]
        status = computer.intcode_computer(input_args)

        if status is not None:
            #print(status)
            if status == 1:
                count += 1
                seen += 1
                if start_updated is False:
                    start = i-3
                start_updated = True
                end_val = i
            world[i][j] = status
    end_val += 3
    width = seen +2
row_count = []
for j in range(800, maxY):
    #print()
    #sys.stdout.write(str(j) + ":")
    row_sum = 0
    for i in range(maxX):
        if world[i][j] == 1:
            row_sum += 1
        #sys.stdout.write(str(world[i][j]))
    row_count.append(row_sum)
    
print("1s is " + str(count))
for i, v in enumerate(row_count):
    print(str(i) + " : " + str(v))

# start at 900 since the rows don't get to 100 beam width until around row 819
for j in range(900, maxY):
    print("checking " + str(j))
    start_row = j-(target_square-1)
    start_column = 0
    end_column = 0
    saw_start = False
    for i in range(maxX):
        if world[i][j] == 1:
            if saw_start is False:
                start_column = i
            saw_start = True
            end_column = i
    #print("start-end is " + str(start_column) + " " + str(end_column))
    if end_column - start_column + 1< target_square:
        #print("not long enough")
        continue

    
    if world[start_column + target_square - 1][start_row] != 1:
        #print("back check failed at row " + str(start_row) + " end col " + str(start_column+target_square-1))
        continue

    for check_row in range(start_row, start_row + target_square):
        if world[start_column][check_row] != 1 and world[start_column + target_square -1][check_row] != 1:
            continue

    print("row " + str(start_row) + " to " + str(j) + " looks good from " + str(start_column) + " " + str(start_column+target_square-1))
    break



    
    

