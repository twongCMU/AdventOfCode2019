#!/usr/bin/python3

import datetime

#test data
data = {1:{'pos' : (-1,0,2), 'vel' : (0,0,0)},
        2:{'pos' : (2,-10,-7), 'vel' : (0,0,0)},
        3:{'pos' : (4,-8,8), 'vel' : (0,0,0)},
        4:{'pos' : (3,5,-1), 'vel' : (0,0,0)}}


# actual data
data = {1:{'pos' : (-17, 9, -5), 'vel' : (0,0,0)},
        2:{'pos' : (-1, 7, 13), 'vel' : (0,0,0)},
        3:{'pos' : (-19, 12, 5), 'vel' : (0,0,0)},
        4:{'pos' : (-6, -6, -4), 'vel' : (0,0,0)}}


print(str(data))
steps = 1
history_dict = {}

# save string for lookup
temp_string = ""
for moon in sorted(data.keys()):
    temp_string += str(moon) + " : " + str(data[moon]['pos'][2]) + str(data[moon]['vel'][2])
history_dict[temp_string] = 1
print(temp_string)
while(1):
    
    # update velocity based on position
    for moon1 in data.keys():
        for moon2 in data.keys():
            
            if moon1 >= moon2:
                continue

            
            (moon1_posX, moon1_posY, moon1_posZ) = data[moon1]['pos']
            (moon1_velX, moon1_velY, moon1_velZ) = data[moon1]['vel']
            
            (moon2_posX, moon2_posY, moon2_posZ) = data[moon2]['pos']
            (moon2_velX, moon2_velY, moon2_velZ) = data[moon2]['vel']
            

            if moon1_posX > moon2_posX:
                moon1_velX -= 1
                moon2_velX += 1
            elif moon1_posX < moon2_posX:
                moon1_velX += 1
                moon2_velX -= 1

            if moon1_posY > moon2_posY:
                moon1_velY -= 1
                moon2_velY += 1
            elif moon1_posY < moon2_posY:
                moon1_velY += 1
                moon2_velY -= 1

            if moon1_posZ > moon2_posZ:
                moon1_velZ -= 1
                moon2_velZ += 1
            elif moon1_posZ < moon2_posZ:
                moon1_velZ += 1
                moon2_velZ -= 1

            data[moon1]['vel'] = (moon1_velX, moon1_velY, moon1_velZ)
            data[moon2]['vel'] = (moon2_velX, moon2_velY, moon2_velZ)

            #print("Moons " + str(moon1) + " and " + str(moon2))
            #print("Vel " + str(data[moon1]['vel']) + " and " + str(data[moon2]['vel']))
    # update position based on velocity
    for moon in data.keys():
        (moon_posX, moon_posY, moon_posZ) = data[moon]['pos']
        (moon_velX, moon_velY, moon_velZ) = data[moon]['vel']

        moon_posX += moon_velX
        moon_posY += moon_velY
        moon_posZ += moon_velZ

        data[moon]['pos'] = (moon_posX, moon_posY, moon_posZ)
            
    #print(str(data))

    # save string for lookup
    temp_string = ""
    for moon in sorted(data.keys()):
        temp_string += str(moon) + " : " + str(data[moon]['pos'][2]) + str(data[moon]['vel'][2])
        
    #print(temp_string)
    if temp_string in history_dict:
        print("duplicate at " + str(steps) + " add one for actual steps ")
        exit()
    history_dict[temp_string] = 1

    steps += 1
    if steps % 100000 == 0:
        print(str(steps) + " at " + str(datetime.datetime.now()))

"""
energy = 0
for moon in data.keys():
    (moon_posX, moon_posY, moon_posZ) = data[moon]['pos']
    (moon_velX, moon_velY, moon_velZ) = data[moon]['vel']

    potential = abs(moon_posX) + abs(moon_posY) + abs(moon_posZ)
    kinetic = abs(moon_velX) + abs(moon_velY) + abs(moon_velZ)

    energy += potential * kinetic

print("Energy is " + str(energy))
"""
