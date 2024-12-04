import re
file = open("in", "r")
result1 = 0
do = True
for line in file:
    list = re.findall(r"don\'t\(\)|do\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)", line)
    for i in list:
        print(i)
        if i == "don't()":
            do = False
            print("disabled")
            continue
        if i == "do()":
            do = True
            print("enabled")
            continue
        if do:
            print("multiplying")
            i = i.replace("mul(", "")
            i = i.replace(")", "")
            nums = i.split(",")
            result1 += int(nums[0]) * int(nums[1])

print (result1)
