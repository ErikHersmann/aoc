from helper import problem_data, throw


points, folds = problem_data.split("\n\n")
points = set([tuple(map(int, line.split(","))) for line in points.splitlines()])
folds = [(line.split()[-1]).split("=") for line in folds.splitlines()]


first = True
for fold in folds:
    axis, value = fold
    value = int(value)
    if axis == "y":
        # We go from value to the biggest x
        new = set()
        while len(points):
            (x, y) = points.pop()
            if y < value:
                new.add((x, y))
            elif y > value:
                # Transform
                new.add((x, value - (y - value)))
            else:
                continue
        points = new
    elif axis == "x":
        # We go from value to the biggest x
        new = set()
        while len(points):
            (x, y) = points.pop()
            if x < value:
                new.add((x, y))
            elif x > value:
                # Transform
                new.add((value - (x - value), y))
            else:
                continue
        points = new
    else:
        throw()
    # print(len(points))
    if first:
        print(f"Part 1: {len(points)}")
        first = False

min_x = 100000
min_y = 100000
max_x = 0
max_y = 0

for point in points:
    (x, y) = point
    max_x = max(x, max_x)
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)

print("Part 2:")
for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        print([" ", "#"][(x, y) in points], end="")
    print("")