from helper import unstripped_problem_data, throw
from termcolor import cprint
from time import sleep

problem_data = unstripped_problem_data
# problem_data = """/>-<\  
# |   |  
# | /<+-\\
# | | | v
# \>+</ |
#   |   ^
#   \<->/"""

# Calculate the list of coordinates of a full loop for each cart
# to detect  reaching the same position save x, y, dir, cart
# if a key is detected again that cart has looped

# cart_id: (direction, next_intersection_choice)
# left, straight, right
carts = []
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

curves = {
    "/": {LEFT: DOWN, RIGHT: UP, DOWN: LEFT, UP: RIGHT},
    "\\": {LEFT: UP, RIGHT: DOWN, DOWN: RIGHT, UP: LEFT},
}
left = {LEFT: DOWN, RIGHT: UP, DOWN: RIGHT, UP: LEFT}
right = {LEFT: UP, RIGHT: DOWN, DOWN: LEFT, UP: RIGHT}
choice = {"left": "straight", "straight": "right", "right": "left"}
initial = {"^": UP, "<": LEFT, "v": DOWN, ">": RIGHT}
problem_data = problem_data.splitlines()
positions = {}
maxx = len(problem_data[0])
maxy = len(problem_data)
for y, line in enumerate(problem_data):
    for x, char in enumerate(line):
        if char in initial:
            carts.append([(x, y), initial[char], "left"])
            positions[(x, y)] = "|" if initial[char] in [UP, DOWN] else "-"
        elif char != " ":
            positions[(x, y)] = char

tick = 0
while tick < 100000:
    pops = []
    for cart_idx, cart in sorted(enumerate(carts), key=lambda x: x[1][0][1]):
        if cart_idx in pops:
            continue
        (pos, direction, intersection_choice) = cart
        (x, y) = pos
        (x_offset, y_offset) = direction
        new_pos = (x + x_offset, y + y_offset)
        assert new_pos in positions, f"Cart: {cart}, new pos: {new_pos}"
        match positions[new_pos]:
            case "/" | "\\":
                direction = curves[positions[new_pos]][direction]
            case "+":
                match intersection_choice:
                    case "left":
                        direction = left[direction]
                    case "right":
                        direction = right[direction]
                intersection_choice = choice[intersection_choice]
        l = [cart[0] for cart in carts]
        if new_pos in l:
            pops.extend([cart_idx, l.index(new_pos)])
            print(f"Crash occurred at {new_pos} at {tick}")
        carts[cart_idx] = [new_pos, direction, intersection_choice]

    if len(pops) > 0:
        print(f"Drawing map... ({tick})")
        cart_pos = [cart[0] for cart in carts]
        for y in range(0, maxy + 1):
            for x in range(0, maxx + 1):
                cprint((positions[(x,y)] if (x, y) in positions else " ") if (x, y) not in cart_pos else (hex(cart_pos.index((x, y)))[-1] if cart_pos.count((x,y)) == 1 else "X"), end="", color="red" if (x, y) in cart_pos else "white")
            print()
        print(f"Finished drawing map... ({tick})")
    for pop in sorted(pops, reverse=True):
        carts.pop(pop)
        print(f"Removing cart: {pop}, remaining carts: {len(carts)}")
    tick += 1
    l = ["|".join(str(x) for x in cart[0]) for cart in carts]
    # print(f"{tick}:", " ".join(l))
    # sleep(0.1)
    # if len(set(l)) != len(l):
    #     print(tick, l)
    #     break
    if len(carts) == 1:
        print(carts[0])
        break
