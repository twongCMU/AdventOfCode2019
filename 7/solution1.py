#!/usr/bin/python3

import itertools

data = [3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

#data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def get_val(arg_index, data_index, modes, data):
    mode = 0
    if arg_index >= len(modes):
        mode = 0
    else:
        mode = modes[arg_index]

    if mode == 0: # position mode - data at index is a pointer to the offset of the actual data
        return data[data[data_index]]

    # immediate mode - return the data found at the index
    return data[data_index]
        
def intcode_computer(input_phase, input_signal, data): 
    cur_index = 0
    output = None
    input_number = 0
    while data[cur_index] != 99:
        #print("At index " + str(cur_index) + " with data " + str(data[cur_index]))

        op = data[cur_index]
        # opcode is the first 2 digits
        opcode = op % 100

        op = int(op/100)
        modes = []
        while op > 0:
            modes.append(op % 10)
            op = int(op/10)

        # add
        if opcode == 1:
            sum = get_val(0, cur_index+1, modes, data) + get_val(1, cur_index+2, modes, data)
            data[data[cur_index+3]] = sum
            cur_index += 4
        # multiply
        elif opcode == 2:
            prod = get_val(0, cur_index+1, modes, data) * get_val(1, cur_index+2, modes, data)
            data[data[cur_index+3]] = prod
            cur_index += 4
        # save
        elif opcode == 3:
            if input_number == 0:
                data[data[cur_index+1]] = input_phase
            elif input_number == 1:
                data[data[cur_index+1]] = input_signal
            else:
                raise 
            cur_index += 2
            input_number += 1
        # output
        elif opcode == 4:
            output = data[data[cur_index+1]]
            cur_index += 2
        # jump if true
        elif opcode == 5:
            if_val = get_val(0, cur_index+1, modes, data)
            jump_to = get_val(1, cur_index+2, modes, data)

            if if_val != 0:
                cur_index = jump_to
            else:
                cur_index += 3

        # jump if false
        elif opcode == 6:
            if_val = get_val(0, cur_index+1, modes, data)
            jump_to = get_val(1, cur_index+2, modes, data)

            if if_val == 0:
                cur_index = jump_to
            else:
                cur_index += 3
        # less than
        elif opcode == 7:
            param1 = get_val(0, cur_index+1, modes, data)
            param2 = get_val(1, cur_index+2, modes, data)

            if param1 < param2:
                data[data[cur_index+3]] = 1
            else:
                data[data[cur_index+3]] = 0

            cur_index += 4
        # equals
        elif opcode == 8:
            param1 = get_val(0, cur_index+1, modes, data)
            param2 = get_val(1, cur_index+2, modes, data)

            if param1 == param2:
                data[data[cur_index+3]] = 1
            else:
                data[data[cur_index+3]] = 0

            cur_index += 4


        else:
            print(data)
            assert data[cur_index] == 99
            
    return output

phase_list = list(itertools.permutations([0,1,2,3,4]))

highest_result = 0
for phase in phase_list:
    
    outputA = intcode_computer(phase[0], 0, data.copy())
    outputB = intcode_computer(phase[1], outputA, data.copy())
    outputC = intcode_computer(phase[2], outputB, data.copy())
    outputD = intcode_computer(phase[3], outputC, data.copy())
    outputE = intcode_computer(phase[4], outputD, data.copy())
    
    if outputE > highest_result:
        highest_result = outputE

print("BEST is " + str(highest_result))
