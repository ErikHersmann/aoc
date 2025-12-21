from collections import defaultdict
from helper import input_data, test_data

first, second = map(lambda x: x.splitlines(), input_data.split("\n\n"))
first = list(map(lambda x: list(map(int, x.split("|"))), first))
second = list(map(lambda x: list(map(int, x.split(","))), second))

d = defaultdict(list)
for line in first:
    d[line[1]].append(line[0])

def part2(update):
    for num in update:
        if len(set(d[num]).intersection(set(update))) == 0:
            continue
        # Case intersect is 
    return 0

total1 = 0
total2 = 0
for update in second:
    dep = set()
    correct = True
    for num in update:
        dep.update(d[num])
        if num in dep:
            correct = False
            break
    if correct:
        # Add middle
        total1 += update[len(update)//2]
    else:
        total2 += part2(update[:])
print(total1)
print(total2)
