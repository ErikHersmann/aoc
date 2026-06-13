from helper import problem_data
from collections import defaultdict

columns = [defaultdict(int) for _ in range(8)]
for line in problem_data.splitlines():
    for idx, c in enumerate(line):
        columns[idx][c] += 1

part_1 = ""
part_2 = ""
for column in columns:
    mmin, mmax = min(column.values()), max(column.values())
    for key, value in column.items():
        if value == mmin:
            part_2 += key
        if value == mmax:
            part_1 += key
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")