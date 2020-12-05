#!/usr/bin/python3

import itertools
from solution2_amp import amplifier

phase_list = list(itertools.permutations([5,6,7,8,9]))

highest_result = 0

for phase in phase_list:
    ampA = amplifier()
    ampB = amplifier()
    ampC = amplifier()
    ampD = amplifier()
    ampE = amplifier()
    is_done = False

    print("for phase " + str(phase))
    outputE = 0
    while not is_done:
        outputA = ampA.intcode_computer(phase[0], outputE)
        outputB = ampB.intcode_computer(phase[1], outputA)
        outputC = ampC.intcode_computer(phase[2], outputB)
        outputD = ampD.intcode_computer(phase[3], outputC)
        is_done = ampA.get_is_done()

        if not is_done:
            outputE = ampE.intcode_computer(phase[4], outputD)
        

        print("going around got " + str(outputE))

    if outputE is not None and outputE > highest_result:
        highest_result = outputE

print("BEST is " + str(highest_result))
