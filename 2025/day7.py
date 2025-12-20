from helper import input_data
from collections import defaultdict

res1 = 0
data = input_data.splitlines()

beams = set()
counts = defaultdict(int)
start_idx = data[0].index("S")
beams.add(start_idx)
counts[start_idx] = 1
for row in range(1, len(data)):
    for col in range(len(data[0])):
        if data[row][col] == "^" and col in beams:
            beams.remove(col)
            for i in [-1, 1]:
                beams.add(col + i)
                counts[col + i] += counts[col]
            res1 += 1
            counts[col] = 0
print(f"Part 1: {res1}")
print(f"Part 2: {sum([val for val in counts.values()])}")