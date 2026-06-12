from collections import defaultdict
from helper import problem_data, throw


def deconstruct(line: str):
    line = line.split()
    offset = 0
    if line[0] == "toggle":
        offset = 1
    match line[1 - offset]:
        case "on":
            action = 1
        case "off":
            action = 0
        case "toggle":
            action = 2
        case _:
            throw()
    start = [int(x) for x in line[2 - offset].split(",")]
    end = [int(x) for x in line[4 - offset].split(",")]
    return action, start, end


IS_PART_ONE = False
lights = [[0 for _ in range(1000)] for _ in range(1000)]
for line in problem_data.splitlines():
    action, start, end = deconstruct(line)
    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            lights[row][col] = (
                (0 if action == 0 or (action == 2 and lights[row][col]) else 1)
                if IS_PART_ONE
                else (max(0, lights[row][col] + (action if action != 0 else -1)))
            )

print(sum([sum(row) for row in lights]))
