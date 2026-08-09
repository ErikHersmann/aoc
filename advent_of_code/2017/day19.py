from helper import transform_flip, LEFT, RIGHT, DOWN_flip, unsanitized_problem_data
from termcolor import cprint
from time import sleep

def visualize(positions_dict, pos):
    for y in range(202):
        for x in range(202):
            key = (x, y)
            if key in positions_dict:
                cprint(positions_dict[key], color="white" if key != pos else "red", end="")
            print(" ", end="")
        print()
    sleep(1.5)
    print("\n\n")
direction = DOWN_flip
positions = {}
cx, cy = 0, 0
for y, line in enumerate(unsanitized_problem_data.splitlines()):
    for x, character in enumerate(line):
        if character != " ":
            positions[(x, y)] = character
        if y == 0 and character == "|":
            cx, cy = x, y
part_1 = ""
should_visualize = False
if should_visualize:
    visualize(positions, (cx, cy))
steps = 1
while True:
    if positions[(cx, cy)].isalpha():
        part_1 += positions[(cx, cy)]
    if (key := (cx + direction[0], cy + direction[1])) in positions:
        (cx, cy) = key
        if should_visualize:
            visualize(positions, (cx, cy))
        steps += 1
        continue
    for offset in [LEFT, RIGHT]:
        new_dir = transform_flip(direction, offset)
        if (cx + new_dir[0], cy + new_dir[1]) in positions:
            direction = new_dir
            break
    else:
        print(f"Part 1: {part_1}")
        print(f"Part 2: {steps}")
        break
