file = open("input", "r")
result = 0
result1 = 0
report= []

def check(report):
    report_sorted = sorted(report)
    report_reversed_sorted = sorted(report, reverse=True)
    if report not in (report_sorted, report_reversed_sorted):
        return False

    for i in range(1, len(report)):
        diff = abs(report[i-1] - report[i])
        if diff == 0 or diff > 3:
            return False
    return True


for line in file:
    report = [int(i) for i in list(line.split())]

    if check(report):
        result += 1

    options = [report[:i] + report[i+1:] for i in range(len(report))]

    for option in options:
        if check(option):
            result1 += 1
            break

print(result1)
