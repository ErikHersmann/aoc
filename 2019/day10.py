from math import gcd, atan

from numpy import arctan
from helper import test_data, test_data_2, input_data
from collections import defaultdict

data = test_data

coords = set()
data = [[x for x in line] for line in data.splitlines()]

for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == "#":
            coords.add((row, col))


def transform(vector) -> tuple:
    divisor = gcd(*vector)
    assert divisor != 0
    return ((vector[0] // divisor, vector[1] // divisor), divisor)


def retransform(unit_vector, scale, current) -> tuple:
    return (current[0] + unit_vector[0] * scale, current[1] + unit_vector[1] * scale)


# Contains all direct neighbors
neighbors = defaultdict(set)
visited = set()

for current in coords:
    (x, y) = current
    potentials = {}  # Direction: length
    for neighbor in coords:
        if neighbor == current:
            continue
        if neighbor in visited:
            if current in neighbors[neighbor]:
                neighbors[current].add(neighbor)
                (unit_vector, scale) = transform((x - neighbor[0], y - neighbor[1]))
                potentials[unit_vector] = (scale, neighbor)
        else:
            (unit_vector, scale) = transform((x - neighbor[0], y - neighbor[1]))
            if unit_vector in potentials and potentials[unit_vector][0] < scale:
                continue
            # else we add it to potentials or update the scale to the smaller new one
            potentials[unit_vector] = (scale, neighbor)

    # Compare vectors being just scaled (hidden) and then add all unscaled ones to the count
    neighbors[current] = neighbors[current].union(
        [neighbor for (unit, (scale, neighbor)) in potentials.items()]
    )
    visited.add(current)


# We get too many neighbors one eight should be a 6 probably, and oe eight should be a 7
# print([f"{key}: {len(val)}" for (key, val) in neighbors.items()])
best = 0
monitoring_station = None

for (key, val) in neighbors.items():
    if len(val) > best:
        best = len(val)
        monitoring_station = key
print(f"part 1: {best}")

# Instead of looking at neighbors, look at not_neigbors aka
# All lines of points
# First assume neighbor_count = count(total_points)
# Count each line as just 1
def sort_clockwise(coordinates: list, start_point: tuple) -> list:
    return sorted(
        coordinates,
    )

# Take monitoring_station and start with neighbors of these
# Make a queue that is properly sorted
# After removing a queue item, append the direct neighbors of that item to the end of the q
q = sort_clockwise(list(neighbors[monitoring_station]), monitoring_station)
# Function for sorting list of coordinates clockwise ?
c = 1
visited = set()
while len(q) > 0:
    cur = q.pop(0)
    if cur in visited: continue
    visited.add(cur)
    if c == 200:
        print(cur)
        break
    # Function for sorting list of coordinates clockwise ?
    q.extend(sort_clockwise(neighbors[cur], cur))
    c += 1


a = {i: i**2 for i in range(2)}; a[2] = 0; send(a)