from helper import short_test, input_data

res1 = 0
data = short_test
data = data.split("\n\n")
shapes, tasks = [x.split(":\n")[1].splitlines() for x in data[:-1]], data[
    -1
].splitlines()
shapes = [
    [[1 if char == "#" else 0 for char in line] for line in shape] for shape in shapes
]
tasks = [
    [
        int(task.split("x")[0]),
        int(task.split("x")[1][0]),
        [int(y) for y in task.split(":")[1].split()],
    ]
    for task in tasks
]

for width, height, req in tasks:
    sanity_check = sum([r * sum([sum(line) for line in shapes[idx]]) for idx, r in enumerate(req)])
    if sanity_check > width*height:
        continue
    grid = [[0 for _ in range(width)] for _ in range(height)]
    # At each step go through the remaining to be placed shapes
    # Go through each point in the grid 
    # Go through each rotation (4) (this includes the flips already)
    # Check if placement possible, if so set grid at those points 1 and continue with next shape (can be greedy since the grid could be flipped or rotated)
    
    res1 += 1
print(res1)