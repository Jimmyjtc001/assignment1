temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]
i = 0
max = 0
while i < 8:
    temp = temperatures_arr[i]
    i = i +1
    if temp > max:
        max = temp

print(max)
#// Note: Values measured in mm Hg.
