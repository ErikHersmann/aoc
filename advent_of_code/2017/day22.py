from helper import problem_data

# Use transformation operation from helper
# rest should be trivial

positions = {}

for y, line in enumerate(problem_data.splitlines()):
    for x, char in enumerate(line):
        p = (x, y)
        if char == "#":
            positions[p] = True
cur = (0, 0)  # TODO ? The virus carrier begins in the middle of the map facing up.

# To avoid detection, the virus carrier works in bursts; in each burst, it wakes up, does some work, and goes back to sleep. The following steps are all executed in order one time each burst:

#     If the current node is infected, it turns to its right. Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)
#     If the current node is clean, it becomes infected. Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)
#     The virus carrier moves forward one node in the direction it is facing.
