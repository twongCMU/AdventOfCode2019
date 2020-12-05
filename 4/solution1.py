#!/usr/bin/python3

start = 353096
end = 843212



good_count = 0
for i in range(start, end+1):
    digits = list(map(int, str(i)))
    has_double = False
    #-1 since we compare d_i and d_i+1
    for d_i in range(len(digits) - 1): 
        if digits[d_i] == digits[d_i+1]:
            if (d_i + 2 >= len(digits) or digits[d_i+2] != digits[d_i]) and (d_i-1<0 or digits[d_i-1]!= digits[d_i]):
                has_double = True
                break

    if has_double is False:
        continue



    has_decrease = False
    for d_i in range(len(digits) - 1): #-1 since we compare d_i and d_i+1
        if digits[d_i+1] < digits[d_i]:
            has_decrease = True
            break
    if has_decrease:
        continue


    good_count += 1


    
print("good is " + str(good_count))
