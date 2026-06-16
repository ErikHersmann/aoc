from helper import input_data

data = input_data
data = [[x for x in a] for a in data.splitlines()]
h = len(data)
w = len(data[0])


def has_neighbors(position: tuple):
    (row, col) = position
    neighbor_count = 0
    if row > 0:
        # TOP
        if data[row - 1][col] == "@":
            neighbor_count += 1
        # TOP LEFT
        if col > 0 and data[row - 1][col - 1] == "@":
            neighbor_count += 1
        # TOP RIGHT
        if col < w - 1 and data[row - 1][col + 1] == "@":
            neighbor_count += 1
    if row < h - 1:
        # BOTTOM
        if data[row + 1][col] == "@":
            neighbor_count += 1
        # BOTTOM LEFT
        if col > 0 and data[row + 1][col - 1] == "@":
            neighbor_count += 1
        # BOTTOM RIGHT
        if col < w - 1 and data[row + 1][col + 1] == "@":
            neighbor_count += 1
    # LEFT
    if col > 0 and data[row][col - 1] == "@":
        neighbor_count += 1
    # RIGHT
    if col < w - 1 and data[row][col + 1] == "@":
        neighbor_count += 1
    return 1 if neighbor_count < 4 else 0

res1 = 0
for row in range(h):
    for col in range(w):
        if data[row][col] != "@":
            continue
        res1 += has_neighbors((row, col))
print(f"Part 1: {res1}")

res2 = 0
previous = -1
iteration = 1
while res2 != previous:
    previous = res2
    for row in range(h):
        for col in range(w):
            if data[row][col] != "@":
                continue
            if has_neighbors((row, col)):
                res2 += 1
                data[row][col] = "."
print(f"Part 2: {res2}")
