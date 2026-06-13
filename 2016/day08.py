from helper import problem_data
from functools import reduce


# TODO: What in the fuck is this code
W, H = 50, 6
pixels = [[0 for _ in range(W)] for _ in range(H)]
for line in problem_data.splitlines():
    line = line.split()
    if line[0] == "rect":
        width, height = map(int, line[1].split("x"))
        for x in range(width):
            for y in range(height):
                pixels[y][x] = 1
    elif line[0] == "rotate":
        is_row = line[1] == "row"
        start = int(line[2].split("=")[-1])
        rotate_by = int(line[4])
        if is_row:
            pixels[start] = [a for l in [pixels[start][-rotate_by:], pixels[start][:-rotate_by]] for a in l]
        else:
            column = [pixels[i][start] for i in range(len(pixels))]
            column = [a for l in [column[-rotate_by:], column[:-rotate_by]] for a in l]
            for i in range(len(pixels)):
                pixels[i][start] = column[i]
        pass
    # Switch i with -by+i for i from 0 to by
print(sum([sum(row) for row in pixels]))

for row in pixels:
    for char in row:
        print(" " if char == 0 else "#", end="")
    print()