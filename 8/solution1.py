#!/usr/bin/python3

import sys

with open("input") as f:
    line = f.readline()

    dimX = 25
    dimY = 6

    line_list = list(map(int, str(line.strip())))
    
    layers = int(len(line_list) / (dimX*dimY))
                     
    print("layers is " + str(layers))

    min_zeros = sys.maxsize
    min_num_ones = 0
    min_num_twos = 0
    for layer in range(layers):
        num_zeros = 0
        num_ones = 0
        num_twos = 0
        start = layer * (dimX*dimY)
        for i in range(dimX*dimY):
            if line_list[start+i] == 0:
                num_zeros += 1
            if line_list[start+i] == 1:
                num_ones += 1
            if line_list[start+i] == 2:
                num_twos += 1

        if num_zeros < min_zeros:
            min_zeros = num_zeros
            min_num_ones = num_ones
            min_num_twos = num_twos

f.close()
print("Min Zeros " + str(min_zeros) + " ones " + str(min_num_ones) + " twos " + str(min_num_twos) + " product " + str(min_num_ones * min_num_twos))
            
            
        
