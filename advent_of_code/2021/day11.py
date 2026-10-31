from helper import problem_data
from copy import deepcopy

# problem_data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526
# """

data  = [[int(c) for c in line] for line in problem_data.splitlines()]
n_row = len(data)
n_col = len(data[0])
target = n_row*n_col

def get_neighbors(tup: tuple):
    neighbors = []
    (r_idx, c_idx) = tup
    # Up check
    if r_idx > 0:
    # TL
        if c_idx > 0:
            neighbors.append((r_idx-1, c_idx-1))
    # T
        neighbors.append((r_idx-1, c_idx))
    # TR
        if c_idx < n_col - 1:
            neighbors.append((r_idx-1, c_idx+1))
    # L
    if c_idx > 0:
        neighbors.append((r_idx, c_idx-1))
    # R
    if c_idx < n_col-1:
        neighbors.append((r_idx, c_idx+1))
    # Down check
    if r_idx < n_row-1:
    # BL 
        if c_idx > 0:
            neighbors.append((r_idx+1, c_idx-1))
    # B
        neighbors.append((r_idx+1, c_idx))
    # BR
        if c_idx < n_col - 1:
            neighbors.append((r_idx+1, c_idx+1))
    return neighbors
# Increase all by one
# Go through data and determine who should flash in each step track via set
# Pop from set and increase others and add the popped to already flashed
# If any of the increased go above 8 we add them to should flash if they haven't already flashed before
# Finally advance to the next step
n = 10000
total_flashes = 0
for step in range(1, n+1):
    temp = deepcopy(data)
    should_flash = set()
    has_flashed = set()
    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            temp[r_idx][c_idx] += 1
            if temp[r_idx][c_idx] > 9:
                should_flash.add((r_idx, c_idx))
    pass
    while len(should_flash):
        next_flash = should_flash.pop()
        has_flashed.add(next_flash)
        neighbors = get_neighbors(next_flash)
        for neighbor in neighbors:
            (r_idx, c_idx) = neighbor
            temp[r_idx][c_idx] += 1
            if neighbor not in has_flashed and temp[r_idx][c_idx] > 9:
                should_flash.add(neighbor)
    total_flashes += len(has_flashed)
    if len(has_flashed) == target:
        print(f"Part 2: {step}")
        exit()
    while len(has_flashed):
        (r_idx, c_idx) = has_flashed.pop()
        temp[r_idx][c_idx] = 0
    pass
    data = temp
    if step == 100:
        print(f"Part 1: {total_flashes}")

print(total_flashes)

# 