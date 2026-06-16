 from helper import short_test, input_data
from math import dist
from collections import defaultdict

res1 = 0
data = input_data
data = [[int(y) for y in x.split(",")] for x in data.splitlines()]
n = len(data)

distances = []
row_map = defaultdict(list)
col_map = defaultdict(list)
inf = 10000000
# Min , Max
col_extrema = [inf, -inf]
row_extrema = [inf, -inf]
for idx1 in range(n):
    for idx2 in range(idx1+1, n):
        distances.append([dist(data[idx1], data[idx2]), idx1, idx2])
        if idx2 -1 == idx1:
            p1, p2 = data[idx1], data[idx2]
            c1, r1 = p1
            c2, r2 = p2
            col_extrema = [min([c1, c2, col_extrema[0]]), max([c1, c2, col_extrema[1]])]
            row_extrema = [min([r1, r2, row_extrema[0]]), max([r1, r2, row_extrema[1]])]
            if c1 != c2:
                assert r1 == r2
                s = sorted([c1, c2])
                if s not in row_map[r1]:
                    row_map[r1].append(s)
            else:
                assert c1 == c2
                s = sorted([r1, r2])
                if s not in col_map[c1]:
                    col_map[c1].append(s)
distances.sort(reverse=True, key=lambda x: x[0])

def check_range(check):
    # Construct 4 sides as intervals
    # Check for a horizontal side:
        # If
    for point in check:
        col, row = point
        found = False
        for row_offset in range(row, row_extrema[0] - 1, -1):
            if row_offset in row_map:
                for start, end in row_map[row_offset]:
                    if start <= col <= end:
                        found = True
                        break
            if found:
                break
        if not found: return False
        found = False
        for row_offset in range(row, row_extrema[1]+1):
            if row_offset in row_map:
                for start, end in row_map[row_offset]:
                    if start <= col <= end:
                        found = True
                        break
            if found:
                break
        if not found: return False
        found = False
        for col_offset in range(col, col_extrema[0] - 1, -1):
            if col_offset in col_map:
                for start, end in col_map[col_offset]:
                    if start <= row <= end:
                        found = True
                        break
            if found:
                break
        if not found: return False
        found = False
        for col_offset in range(col, col_extrema[1] + 1):
            if col_offset in col_map:
                for start, end in col_map[col_offset]:
                    if start <= row <= end:
                        found = True
                        break
            if found:
                break
        if not found: return False
    return True


for dist_idx in range(len(distances)):
    point_1 = data[distances[dist_idx][1]]
    c1, r1 = point_1
    point_2 = data[distances[dist_idx][2]]
    c2, r2 = point_2
    if r1 == r2 or c1 == c2: continue
    height = abs(point_1[0] - point_2[0]) + 1
    width = abs(point_1[1] - point_2[1]) + 1
    exist = [point_1, point_2]
    minrow, maxrow = min(r1, r2), max(r1, r2)
    mincol, maxcol = min(c1, c2), max(c1, c2)
    check = []
    for point in [[mincol, minrow], [maxcol, minrow], [mincol, maxrow], [maxcol, maxrow]]:
        if point in exist: continue
        check.append(point)
    assert len(check) == 2
    if check_range(check):
        print(f"{point_1} {point_2} {check}")
        print(f"Height: {height}\tWidth: {width}")
        print(f"Area: {height * width}")
        break
# 1902003180 is too high

# Concave structures can still ruin this approach