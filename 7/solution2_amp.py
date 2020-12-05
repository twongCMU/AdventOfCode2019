#!/usr/bin/python3

class amplifier:
    def __init__(self):
        self.data = [3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

        #self.data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        self.cur_index = 0
        self.input_number = 0
        self.is_done = False
    def get_val(self, arg_index, data_index, modes):
        mode = 0
        if arg_index >= len(modes):
            mode = 0
        else:
            mode = modes[arg_index]

        if mode == 0: # position mode - data at index is a pointer to the offset of the actual data
            return self.data[self.data[data_index]]

        # immediate mode - return the data found at the index
        return self.data[data_index]

    def get_is_done(self):
        return self.is_done
    
    def intcode_computer(self, input_phase, input_signal):
        output = None
        
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
                self.data[self.data[self.cur_index+3]] = sum
                self.cur_index += 4
            # multiply
            elif opcode == 2:
                prod = self.get_val(0, self.cur_index+1, modes) * self.get_val(1, self.cur_index+2, modes)
                self.data[self.data[self.cur_index+3]] = prod
                self.cur_index += 4
            # save
            elif opcode == 3:
                if self.input_number == 0:
                    self.data[self.data[self.cur_index+1]] = input_phase
                elif self.input_number == 1:
                    self.data[self.data[self.cur_index+1]] = input_signal
                else:
                    raise 
                self.cur_index += 2
                self.input_number += 1
                if self.input_number > 1:
                    self.input_number = 1
            # output
            elif opcode == 4:
                output = self.data[self.data[self.cur_index+1]]
                self.cur_index += 2
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
                    self.data[self.data[self.cur_index+3]] = 1
                else:
                    self.data[self.data[self.cur_index+3]] = 0

                self.cur_index += 4
            # equals
            elif opcode == 8:
                param1 = self.get_val(0, self.cur_index+1, modes)
                param2 = self.get_val(1, self.cur_index+2, modes)

                if param1 == param2:
                    self.data[self.data[self.cur_index+3]] = 1
                else:
                    self.data[self.data[self.cur_index+3]] = 0

                self.cur_index += 4


            else:
                print(data)
                assert self.data[self.cur_index] == 99
                self.is_done = True
                
        if self.data[self.cur_index] == 99:
            self.is_done = True
            
        return None
