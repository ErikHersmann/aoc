from helper import problem_data
from collections import defaultdict


print(f"Part 1: {sum(int(num) for num in problem_data.splitlines())}")

data = [int(x) for x in problem_data.splitlines()]
visited = set()
cur = 0
while True:
    for num in data:
        cur += num
        if cur in visited:
            print(f"Part 2: {cur}")
            exit(0)
        visited.add(cur)
