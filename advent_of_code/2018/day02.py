from helper import problem_data
from collections import defaultdict
from math import prod

mult = [0,0]
for line in problem_data.splitlines():
    d = defaultdict(int)
    for c in line:
        d[c] += 1
    two, three = False, False
    for key, value in d.items():
        if value == 2:
            two = True
        if value == 3:
            three = True
    mult[0] += 1 if two else 0
    mult[1] += 1 if three else 0

print(f"Part 1: {prod(mult)}")

for i in problem_data.splitlines():
    for j in problem_data.splitlines():
        if i == j: 
            continue
        error = []
        for idx in range(len(i)):
            if i[idx] != j[idx]:
                error.append(idx)
                if len(error) > 1:
                    break
        if len(error) == 1:
            # print(i)
            # print(j)
            print(f"Part 2: {j[:error[0]]}{j[error[0]+1:]}")
            exit(0)