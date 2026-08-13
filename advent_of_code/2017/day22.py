from helper import problem_data, LEFT, RIGHT, UP_flip, DOWN_flip, transform_flip
from termcolor import cprint
from enum import Enum

class State(Enum):
    clean = 0,
    weakened = 1,
    infected = 2,
    flagged = 3

positions = {}
initials = set()
direction = UP_flip
for y, line in enumerate(problem_data.splitlines()):
    for x, char in enumerate(line):
        p = (x, y)
        if char == "#":
            positions[p] = State.infected
            initials.add(p)
cur = (x//2, y//2)

def visualize(positions, cur):
    for y in range(-5, 5):
        for x in range(-5, 10):
            if (x,y)==cur:
                cprint("#" if (x,y) in positions else "_", end="", color="red")
            else:
                if (x,y) not in positions:
                    print(" ", end="")
                    continue
                match positions[(x,y)]:
                    case State.clean:
                        print(" ", end="")
                    case State.infected:
                        print("#", end="")
                    case State.flagged:
                        print("F", end="")
                    case State.weakened:
                        print("W", end="")
        print()

infected = 0
iteration = 0
while iteration < 10000000:
    if cur not in positions:
        positions[cur] = State.clean
    match positions[cur]:
        case State.clean:
            direction = transform_flip(direction, LEFT)
            positions[cur] = State.weakened
            pass
        case State.flagged:
            direction = transform_flip(direction, DOWN_flip)
            positions.pop(cur)
        case State.infected:
            direction = transform_flip(direction, RIGHT)
            positions[cur] = State.flagged
        case State.weakened:
            positions[cur] = State.infected
            infected += 1
    cur = (cur[0]+direction[0], cur[1]+direction[1])
    iteration += 1
    if not iteration%100000:
        print(iteration)

print(infected)