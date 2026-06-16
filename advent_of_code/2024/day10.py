from collections import defaultdict
from turtle import down
from helper import input_data, test_data

# First find all 0s
# for each zero recurse with (tile, current height) and do this for all 4 directions if not oob
# If reached 9 or no direction has current height + 1 return 1 or 0 respectively
# Return sum of all 4 directions of initial recursion
# Do this for all 0s
# return sum for all 0s

data = test_data
data = [[int(a) for a in b] for b in input_data.splitlines()]
h,w = len(data), len(data[0])
UP, LEFT, RIGHT, DOWN = (-1, 0), (0, -1), (0, 1), (1, 0)

def oob(pos):
    (r, c) = pos
    return r < 0 or c < 0 or r > h-1 or c > w-1

def trailheadscore(r, c):
    peaks = set()
    def search(r,c, height):
        # This returns all none out of bound neighbors for r, c that are taller by one
        def get_dirs(r, c):
            # If UP not oob and height + 1: append
            retval = []
            for pos in [(r+UP[0], c+UP[1]), (r+LEFT[0], c+LEFT[1]), (r+RIGHT[0], c+RIGHT[1]), (r+DOWN[0], c+DOWN[1])]:
                if not oob(pos) and data[pos[0]][pos[1]]-1 == data[r][c]:
                    retval.append(pos)
            return retval

        if data[r][c] == 9:
            peaks.add((r, c))
            return 1
        dirs = get_dirs(r, c)
        if len(dirs) == 0: 
            return 0
        paths = 0
        for (ri, ci) in dirs:
            paths += search(ri, ci, height+1)
        return paths
    result = search(r, c, 0)
    return (len(peaks), result)

totals = [0,0]
for r in range(h):
    for c in range(w):
        if data[r][c] == 0:
            totals = [x + y for x, y in zip(totals, trailheadscore(r, c))]

print(totals[0])
print(totals[1])
