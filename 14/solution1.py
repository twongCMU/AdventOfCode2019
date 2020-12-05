#!/usr/bin/python3
import math
f = open("input",'r')

lines = f.readlines()

f.close()

reactions_dict = {}
for line in lines:
    print(line)
    (inputs, output) = line.strip().split('=>')

    inputs = inputs.strip()
    output = output.strip()

    input_list = inputs.split(', ')

    (output_quantity, output_chemical) = output.split(' ')

    assert output_chemical not in reactions_dict
    reactions_dict[output_chemical] = {}
    reactions_dict[output_chemical]["output_quantity"] = int(output_quantity)
    reactions_dict[output_chemical]["inputs"] = []
    
    for input in input_list :
        (input_quantity, input_chemical) = input.split(' ')
        
        reactions_dict[output_chemical]["inputs"].append((int(input_quantity), input_chemical))


requirements_dict = {}
requirements_dict["FUEL"] = 2876992
requirements_dict["ORE"] = 0
fuel_count = 1
num_req = 0

for chem in reactions_dict.keys():
    if chem not in requirements_dict:
        requirements_dict[chem] = 0

while 1:

    chem = None
    for chem_try in requirements_dict.keys():
        # if requirement, produce it        
        if requirements_dict[chem_try] > 0 and chem_try != "ORE":
            chem = chem_try
            break

    #if requirements_dict["ORE"] > 1000000000000:
    #    # if there's requirements left we didn't finish making this fuel
    #    if chem is not None:
    #        fuel_count -= 1
    #    break

    # if there are no required chems, add a FUEL
    if chem == None:
        # for part 1
        print("ore " + str(requirements_dict["ORE"]))
        if requirements_dict["ORE"] > 1000000000000:
            print("OVER")
        exit()

        # if requirements are resolved, add a new FUEL
        fuel_count += 1
        requirements_dict["FUEL"] = 1
        chem = "FUEL"
        print("Fuel: " + str(fuel_count) + " Ore: " + str(requirements_dict["ORE"]))


    output_quantity = reactions_dict[chem]["output_quantity"]
    inputs = reactions_dict[chem]["inputs"]

    # if multiple copies of the reaction can produce less than what we need, do it to save time
    multiplier = 1
    if output_quantity < requirements_dict[chem]:
        multiplier = int(requirements_dict[chem]/output_quantity)

    # we've produced the chem, remove it from the requirements
    requirements_dict[chem] -= output_quantity * multiplier

    # put the inputs into the requirements
    for input in inputs:
        (input_quantity, input_chemical) = input
        input_quantity *= multiplier

        requirements_dict[input_chemical] += input_quantity

print(str(requirements_dict))
print("Fuel made " + str(fuel_count))

