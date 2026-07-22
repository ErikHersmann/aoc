from helper import problem_data
from sys import setrecursionlimit

setrecursionlimit(10**6)
nodes = []
d_nodes = {}
start = (0, 0)
for idx, line in enumerate(problem_data.splitlines()):
    if idx <= 1:
        continue
    # Filesystem              Size  Used  Avail  Use%
    (name, size, used, available, percent) = line.split()
    (size, used, available) = map(lambda x: int(x.strip("T")), [size, used, available])
    name = tuple(map(lambda x: int(x[1:]), name.split("-")[-2:]))
    nodes.append([name, size, used, available, percent])
    d_nodes[name] = [size, used, available, percent]
    if name[0] > start[0]:
        start = name
    if used == 0:
        empty = name


pass
viable = 0
for node1 in nodes:
    for node2 in nodes:
        if node1[0] == node2[0] or node1[2] == 0 or node1[2] > node2[3]:
            continue
        viable += 1
print(f"Part 1: {viable}")

# part 2: DP should be doable tbh

seen = dict()
# Move to all directions
# Find 0 block (there is only one) and move to the left in front if needed (maybe there is enough space)
def get_neighbors(position: tuple):
    global d_nodes
    (x, y) = position
    return [pos for pos in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if pos in d_nodes]

target = (0, 0)
limit = 40
def dp(payload_position, empty_position, moves):
    if payload_position in seen and seen[payload_position] <= moves or moves > limit:
        return
    seen[(payload_position, empty_position)] = moves
    if payload_position == target:
        return
    for payload_neighbor in get_neighbors(payload_position):
        # Move payload if neighbor is a free space
        if payload_neighbor == empty_position:
            dp(payload_neighbor, payload_position, moves+1)

    (px, py), (ex, ey) = payload_position, empty_position
    
    for empty_neighbor in get_neighbors(empty_position):
        if empty_neighbor != payload_position:
            dp(payload_position, empty_neighbor, moves+1)

dp(start, empty, 0)
print(seen)