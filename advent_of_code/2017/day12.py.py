from helper import problem_data
from collections import deque

unique_groups = []
for line in problem_data.splitlines():
    line = line.replace(" <-> ", " ").replace(",", "").split()
    unique_groups.append(set([int(x) for x in line]))

n = 0
while n != len(unique_groups):
    n = len(unique_groups)
    for i in range(len(unique_groups)):
        for j in range(i+1, len(unique_groups)):
            if j < len(unique_groups) and len(unique_groups[i].intersection(unique_groups[j])) > 0:
                unique_groups[i] = unique_groups[i].union(unique_groups.pop(j))


print(f"Part 1: {sum([len(group) for group in unique_groups if 0 in group])}")
print(f"Part 2: {len(unique_groups)}")