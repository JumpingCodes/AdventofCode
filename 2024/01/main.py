from pip._vendor.rich import print
file = open("list.txt", "r")
result0 = 0
result1 = 0
leftlist = []
rightlist = []


for line in file:
    if line.strip() == "":
        break
    parts = line.split()
    part1 = int(parts[0])
    part2 = int(parts[1])
    leftlist.append(part1)
    rightlist.append(part2)
leftlist.sort()
rightlist.sort()

for i in range(len(leftlist)):
    result0 += abs(leftlist[i] - rightlist[i])
print(result0)

for i in range(len(leftlist)):
    result1 += leftlist[i] * rightlist.count(leftlist[i])
print(result1)
