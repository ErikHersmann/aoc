from sys import maxsize
from collections import defaultdict
from termcolor import cprint, COLORS

problem_data = 1350

# (x, y)
target = (31, 39)


# Find x*x + 3*x + 2*x*y + y + y*y.
# Add the office designer's favorite number (your puzzle input).
# Find the binary representation of that sum; count the number of bits that are 1.
#     If the number of bits that are 1 is even, it's an open space.
#     If the number of bits that are 1 is odd, it's a wall.
def is_wall(pos):
    (x, y) = pos
    step_1 = x**2 + 3 * x + 2 * x * y + y + y**2
    step_2 = step_1 + problem_data
    step_3 = bin(step_2)
    return step_3.count("1") % 2 == 1


w, h = 60, 42
map = [[is_wall((x_i, y_i)) for x_i in range(w)] for y_i in range(h)]


visited = defaultdict(lambda: maxsize)
paths = []


def oob(pos):
    (x, y) = pos
    return x >= w or y >= h or x < 0 or y < 0 or map[y][x]


def dp(pos, cost, path):
    if oob(pos) or visited[pos] <= cost:
        return
    if pos == target:
        visited[target] = min(visited[target], cost)
        paths.append((cost, path))
        return
    visited[pos] = cost
    path.append(pos)
    dp((pos[0] - 1, pos[1]), cost + 1, path[::])
    dp((pos[0] + 1, pos[1]), cost + 1, path[::])
    dp((pos[0], pos[1] - 1), cost + 1, path[::])
    dp((pos[0], pos[1] + 1), cost + 1, path[::])


def visualize():
    for row_idx, row in enumerate(map):
        cprint(f"{row_idx:02}", "white", end=" ")
        for col_idx, element in enumerate(row):
            if (col_idx, row_idx) == target:
                cprint("T", "red", end="")
            elif (col_idx, row_idx) in paths[3][1]:
                cprint("O", "yellow", end="")
            elif (col_idx, row_idx) in paths[2][1]:
                cprint("O", "blue", end="")
            elif (col_idx, row_idx) in paths[1][1]:
                cprint("O", "cyan", end="")
            elif (col_idx, row_idx) in paths[0][1]:
                cprint("O", "green", end="")
            else:
                print(f'{"#" if element else "_"}', end="")
        print()


dp((1, 1), 0, [])
print(visited[target])
print(sum([1 for key in visited if visited[key] <= 50]))
visualize()
