from helper import problem_data
from collections import defaultdict

# we are given top left, width, height

# problem_data = """#1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2"""
#  Just brute force, the map is only 1000x1000
seen = defaultdict(int)
for idx, rectangle in enumerate(problem_data.splitlines()):
    x, y, w, h = map(int, rectangle.split(" @ ")[1].replace("x", " ").replace(":", "").replace(",", " ").split())
    for xi in range(x, x+w):
        for yi in range(y, y+h):
            seen[(xi, yi)] += 1
            if seen[(xi, yi)] >= 2:
                overlap = True

total = 0
for value in seen.values():
    if value >= 2:
        total += 1
print(f"Part 1: {total}")


for idx, rectangle in enumerate(problem_data.splitlines()):
    x, y, w, h = map(int, rectangle.split(" @ ")[1].replace("x", " ").replace(":", "").replace(",", " ").split())
    overlap = False
    for xi in range(x, x+w):
        for yi in range(y, y+h):
            if seen[(xi, yi)] >= 2:
                overlap = True
    if not overlap:
        print(f"Part 2: {idx+1}")

