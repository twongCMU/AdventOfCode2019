#!/usr/bin/python3

import math
with open("input") as f:
    line = f.readline()

    data_orig = line.strip().split(',')
    
    for i in range(len(data_orig)):
        data_orig[i] = int(data_orig[i])
    print(data_orig)


    for i in range(100):
        for j in range(100):
            data = data_orig.copy()
            cur_index = 0
            data[1] = i
            data[2] = j

            while data[cur_index] != 99:
                #print("At index " + str(cur_index) + " with data " + str(data[cur_index]))
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


            print("Trying " + str(i) + " and " + str(j) + " and got " + str(data[0]))
            if data[0] == 19690720:
                print("DONE")
                print(str(i) +  " " + str(j))
                exit()

