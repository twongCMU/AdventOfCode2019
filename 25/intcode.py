#!/usr/bin/python3

import sys

class intcode:
    # run_until_output: True = return output and stop; False= don't stop
    def __init__(self, data, run_until_output):
        self.data = data

        #self.data=[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        #self.data=[1102,34915192,34915192,7,4,7,99,0]
        #self.data=[104,1125899906842624,99]
        self.cur_index = 0
        self.input_number = 0
        self.is_done = False
        self.relative_base = 0

        temp_arr = [0] * 1000
        self.data.extend(temp_arr)
        
    def get_val(self, mode_index, data_index, modes):
        position = self.get_position(mode_index, data_index, modes)
        return self.data[position]

    def set_val(self, mode_index, data_index, modes, value):
        position = self.get_position(mode_index, data_index, modes)
        self.data[position] = value
    
    def get_position(self, mode_index, data_index, modes):
        mode = 0
        if mode_index >= len(modes):
            mode = 0
        else:
            mode = modes[mode_index]

        if mode == 0: # position mode - data at index is a pointer to the offset of the actual data
            return self.data[data_index]
        if mode == 1:
            # immediate mode - return the data found at the index
            return data_index
        if mode == 2:
            # relative mode
            return self.relative_base +  self.data[data_index]


    def get_is_done(self):
        return self.is_done
    
    def intcode_computer(self, args_list):
        output = None
        self.input_number = 0
        while self.data[self.cur_index] != 99:

            op = self.data[self.cur_index]
            # opcode is the first 2 digits
            opcode = op % 100

            op = int(op/100)
            modes = []
            while op > 0:
                modes.append(op % 10)
                op = int(op/10)

            # add
            if opcode == 1:
                sum = self.get_val(0, self.cur_index+1, modes) + self.get_val(1, self.cur_index+2, modes)
                self.set_val(2, self.cur_index+3, modes, sum)
                #self.data[self.data[self.cur_index+3]] = sum
                self.cur_index += 4
            # multiply
            elif opcode == 2:
                prod = self.get_val(0, self.cur_index+1, modes) * self.get_val(1, self.cur_index+2, modes)
                self.set_val(2, self.cur_index+3, modes, prod)
                #self.data[self.data[self.cur_index+3]] = prod
                self.cur_index += 4
            # save input
            elif opcode == 3:
                #print("PROMPT  " + str(self.input_number) + " giving " + str(str(args_list[self.input_number])))

                if self.input_number >= len(args_list):
                    #print("not enough" + str(self.input_number) + " " + str(len(args_list)))
                    return None

                #print("PROMPT  " + str(self.input_number) + " giving " + str(str(args_list[self.input_number])))
                self.set_val(0, self.cur_index+1, modes, args_list[self.input_number])

                self.cur_index += 2
                self.input_number += 1

                return None

            # output
            elif opcode == 4:
                output = self.get_val(0, self.cur_index+1, modes)
                #output = self.data[self.data[self.cur_index+1]]
                self.cur_index += 2
                sys.stdout.write(chr(output))
                return output
            # jump if true
            elif opcode == 5:
                if_val = self.get_val(0, self.cur_index+1, modes)
                jump_to = self.get_val(1, self.cur_index+2, modes)

                if if_val != 0:
                    self.cur_index = jump_to
                else:
                    self.cur_index += 3

            # jump if false
            elif opcode == 6:
                if_val = self.get_val(0, self.cur_index+1, modes)
                jump_to = self.get_val(1, self.cur_index+2, modes)

                if if_val == 0:
                    self.cur_index = jump_to
                else:
                    self.cur_index += 3
            # less than
            elif opcode == 7:
                param1 = self.get_val(0, self.cur_index+1, modes)
                param2 = self.get_val(1, self.cur_index+2, modes)

                if param1 < param2:
                    self.set_val(2, self.cur_index+3, modes, 1)
                    #self.data[self.data[self.cur_index+3]] = 1
                else:
                    self.set_val(2, self.cur_index+3, modes, 0)
                    self.data[self.data[self.cur_index+3]] = 0

                self.cur_index += 4
            # equals
            elif opcode == 8:
                param1 = self.get_val(0, self.cur_index+1, modes)
                param2 = self.get_val(1, self.cur_index+2, modes)

                if param1 == param2:
                    self.set_val(2, self.cur_index+3, modes, 1)
                    #self.data[self.data[self.cur_index+3]] = 1
                else:
                    self.set_val(2, self.cur_index+3, modes, 0)
                    #self.data[self.data[self.cur_index+3]] = 0

                self.cur_index += 4

            elif opcode == 9:
                param1 = self.get_val(0, self.cur_index+1, modes)
                self.relative_base += param1
                self.cur_index += 2
            else:
                assert self.data[self.cur_index] == 99
                self.is_done = True
                
        if self.data[self.cur_index] == 99:
            self.is_done = True
            
        return None
