from day10 import knot_hash
from collections import defaultdict, deque
from helper import UP, DOWN, RIGHT, LEFT

problem_data = "oundnydw"

positions = set()
for row_idx in range(128):
    knot_hash_value = knot_hash(f"{problem_data}-{row_idx}")
    col_idx = 0
    for hex_digit_idx in range(0, 32, 2):
        for bit in (bin(int(knot_hash_value[hex_digit_idx:hex_digit_idx+2], base=16))[2:]).zfill(8):
            if bit == "1":
                positions.add((col_idx, row_idx))
            col_idx += 1

def get_neighbors(position):
    neighbors = []
    if position in positions:
        positions.remove(position)
    for x, y in [UP, LEFT, DOWN, RIGHT]:
        if (key:= (position[0]+x, position[1]+y)) in positions:
            neighbors.append(key)
            positions.remove(key)
    return neighbors

def exhaust(position):
    q = deque([position])
    while len(q) > 0:
        position = q.pop()
        q.extend(get_neighbors(position))

print(f"Part 1: {len(positions)}")
region_idx = 0
for row in range(128):
    for col in range(128):
        key = (col, row)
        if key in positions:
            exhaust(key)
            region_idx += 1
print(f"Part 2: {region_idx}")