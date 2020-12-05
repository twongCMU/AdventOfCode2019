#!/usr/bin/python3

data = "59705379150220188753316412925237003623341873502562165618681895846838956306026981091618902964505317589975353803891340688726319912072762197208600522256226277045196745275925595285843490582257194963750523789260297737947126704668555847149125256177428007606338263660765335434914961324526565730304103857985860308906002394989471031058266433317378346888662323198499387391755140009824186662950694879934582661048464385141787363949242889652092761090657224259182589469166807788651557747631571357207637087168904251987880776566360681108470585488499889044851694035762709053586877815115448849654685763054406911855606283246118699187059424077564037176787976681309870931"
phases = 100
phase2_offset = 5970537

data = "80871224585914546619083218645595"
phases = 100

data = "03036732577212944063491565474664"
phase2_offset = 303673
phases = 10

# for part 2
data *= 10000

new_data = []
for d in data:
    new_data.append(int(d))

data = new_data

base_pattern = [0,1,0,-1]

for phase in range(phases):
    print("Computing phase " + str(phase))
    new_data = []

    #compute each digit
    for i in range(len(data)):

        # generate pattern for this digit
        pattern = []
        for p in base_pattern:
            # i+1 because the first item is repeated once
            pattern.extend(([p]*(i+1)))

        # offset is 1 because we skip the first pattern value
        pattern_offset = 1

        value = 0
        # compute the FFT
        for digit in data:
            value += digit * pattern[pattern_offset]
            pattern_offset += 1
            if pattern_offset >= len(pattern):
                pattern_offset = 0

        value = abs(value)
        # mod 10 because we only keep the last digit
        new_data.append(value % 10)

    data = new_data
    print("phase " + str(phase+1) + " value " + str(data))
        
        
    
#for i in range(8):
#    print(str(data[phase2_offset + i]))
