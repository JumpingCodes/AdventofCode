file = open("in", "r")
firstpart = True
updates = []
rules = []
pagenumbers = 0

for line in file:
    if line == "\n":
        firstpart = False
    line = line.strip()
    if line == "":
        continue
    if firstpart:
        rules.append(tuple(line.split("|")))
    else:
        updates.append((line.split(",")))


def order(update):
    i = 0
    j = 0
    while(i < len(update)):
        j = i + 1
        while(j < len(update)):
            if (update[i], update[j]) in rules:
                j += 1
                continue
            else:
                tmp = update[i]
                update[i] = update[j]
                update[j] = tmp
                j = i + 1
        i += 1

def check(update):
    relations = []
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            relations.append((update[i], update[j]))

    for relation in relations:
        if relation not in rules:
            return False
    return True


for update in updates:
    if not check(update):
        order(update)
        pagenumbers += int(update[int((len(update)-1)/2)])
    if check(update):
        #pagenumbers += int(update[int((len(update)-1)/2)])
        pass
print (pagenumbers)
