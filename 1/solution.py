#!/usr/bin/python3

import math

def fuel_needed(mass):
    ret = math.floor(mass/3.0) - 2
    if ret < 0:
        ret = 0
    return ret

total_fuel = 0
with open("input") as f:
    line = f.readlines()

    for l in line:
        fuel_one = 0
        mass = int(l.strip())
        
        fuel = fuel_needed(mass)

        fuel_one += fuel

        while fuel > 0:
            # if fuel_needed returns 0 it has no effect to the sum
            # so we can add it
            fuel = fuel_needed(fuel)
            fuel_one += fuel
        print(fuel_one)
        total_fuel += fuel_one

print("Total: " + str(total_fuel))
        
    

