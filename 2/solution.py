#!/usr/bin/python3

import math
with open("input") as f:
    line = f.readline()

    data = line.strip().split(',')

    cur_index = 0

    for i in range(len(data)):
        data[i] = int(data[i])
    print(data)
    
    # fix data to pre-alarm
    data[1] = 12
    data[2] = 2
    
    
    while data[cur_index] != 99:
        print("At index " + str(cur_index) + " with data " + str(data[cur_index]))
        # add
        if data[cur_index] == 1:
            sum = data[data[cur_index+1]] + data[data[cur_index+2]]
            data[data[cur_index+3]] = sum
            cur_index += 4
        # multiply
        elif data[cur_index] == 2:
            prod = data[data[cur_index+1]] * data[data[cur_index+2]]
            data[data[cur_index+3]] = prod
            cur_index += 4
        else:
            assert data[cur_index] == 99
        print(data)

            
        

