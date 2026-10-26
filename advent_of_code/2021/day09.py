from helper import problem_data
from collections import deque
from math import prod

def get_neighbors(r, c, points):
    neighbors = []
    coords = []
    if r > 0:
        neighbors.append(points[r - 1][c])
        coords.append((r-1, c))
    if r < len(points) - 1:
        neighbors.append(points[r + 1][c])
        coords.append((r+1, c))
    if c > 0:
        neighbors.append(points[r][c - 1])
        coords.append((r, c-1))
    if c < len(points[0]) - 1:
        neighbors.append(points[r][c + 1])
        coords.append((r, c+1))
    assert 5 > len(neighbors) > 1, f"{r}\t{c}"
    return neighbors, coords


points = [[int(c) for c in line] for line in problem_data.splitlines()]

local_minima = set()
part_1 = 0
for r, row in enumerate(points):
    for c, point in enumerate(row):
        neighbors, _ = get_neighbors(r, c, points)
        if all([n > point for n in neighbors]):
            part_1 += point + 1
            local_minima.add((r, c))
print(f"Part 1: {part_1}")

basins = []
while len(local_minima):
    queue = deque([local_minima.pop()])
    basins.append(set())
    while len(queue):
        cur = queue.popleft()
        basins[-1].add(cur)
        vals, coords = get_neighbors(cur[0], cur[1], points)
        for val, coord in zip(vals, coords):
            if val != 9 and val > points[cur[0]][cur[1]] and coord not in basins[-1]:
                queue.append(coord)
                basins[-1].add(coord)

print(f"Part 2: {prod(sorted([len(basin) for basin in basins], reverse=True)[:3])}")