from collections import defaultdict
from helper import problem_data

# problem_data = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# """


points = defaultdict(int)
part_2 = False
for line in problem_data.splitlines():
# 956,649 -> 956,593
    l,r = line.split(" -> ")
    l = list(map(int, l.split(",")))
    r = list(map(int, r.split(",")))
    if l[0] == r[0]:
        ys = [l[1], r[1]]
        for y in range(min(ys), max(ys)+1):
            points[(l[0], y)] += 1
    elif l[1] == r[1]:
        xs = [l[0], r[0]]
        for x in range(min(xs), max(xs)+1):
            points[(x, l[1])] += 1
    elif part_2:
        if l[0] > r[0]:
            l, r = r, l
        up = l[1] < r[1]
        points[tuple(l)] += 1
        while l[0] != r[0]:
            l = (l[0] + 1, l[1] + (1 if up else -1))
            points[tuple(l)] += 1

total = 0
for point in points.values():
    if point >= 2:
        total += 1
    
# for point in points:
#     print(point, points[point])
print(total)