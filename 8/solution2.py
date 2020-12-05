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
            

final_image = []
for i in range(dimX*dimY):
    pixel = -1
    for layer in range(layers):
        if line_list[layer*dimX*dimY + i] == 0:
            pixel = 0
            break        
        if line_list[layer*dimX*dimY + i] == 1:
            pixel = 1
            break

        # 2 is transparent and we continue to the next layer
    final_image.append(pixel)

for j in range(dimY):
        print("")
        for i in range(dimX):


            sys.stdout.write(str(final_image[j*dimX + i]))
