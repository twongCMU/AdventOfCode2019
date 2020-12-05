#!/usr/bin/python3



def get_score(data, current):
    count = 0

    for o in data[current].keys():
        count += data[current][o]
        if o in data:
            count += get_score(data, o)
        
    return count

def set_score(data, current, score):
    for o in data[current].keys():
        data[current][o] = score
        if o in data:
            set_score(data, o, score + 1)

def get_path(data, current, key):
    for o in data[current].keys():
        if o == key:
            print("Returning key at " + current)
            return [o]
        
        if o in data:
            path = get_path(data, o, key)

            if path is not None:
                path.append(o)
                return path
    return None

            
with open("input") as f:
    line = f.readlines()

    data = {}
    
    for l in line:
        (mass, orbiter) = l.strip().split(')')

        if mass not in data:
            data[mass] = {}

        data[mass][orbiter] = 0



f.close()
current = "COM"

print(data)
set_score(data, current, 1)

count = get_score(data, current)

print("Count is " + str(count))
    
path_you = get_path(data, "COM", "YOU")
path_san = get_path(data, "COM", "SAN")


for i, node in enumerate(path_you):
    if node in path_san:
        print("Overlap at " + node + " for " + str(i+path_san.index(node)-2))
        exit()
    
        
