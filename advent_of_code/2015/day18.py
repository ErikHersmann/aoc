from helper import problem_data
from copy import deepcopy

# Make a copy at each iteration
def make_lights():
    lights = []
    for row in problem_data.splitlines():
        lights.append([])
        for col in row:
            lights[-1].append(col == "#")
    return lights

def get_neighbors_that_are_on(lights, row_idx, col_idx):
    neighbors = []
    if row_idx > 0 and col_idx > 0:
        #  TL
        neighbors.append(lights[row_idx-1][col_idx-1])
    if row_idx > 0:
        # T
        neighbors.append(lights[row_idx-1][col_idx])
    if row_idx > 0 and col_idx < len(lights[0])-1:
        # TR
        neighbors.append(lights[row_idx-1][col_idx+1])
    if col_idx > 0:
        # L
        neighbors.append(lights[row_idx][col_idx-1])
    if row_idx < len(lights)-1 and col_idx > 0:
        # BL
        neighbors.append(lights[row_idx+1][col_idx-1])
    if row_idx < len(lights)-1:
        # B
        neighbors.append(lights[row_idx+1][col_idx])
    if row_idx < len(lights)-1 and col_idx < len(lights[0])-1:
        # BR
        neighbors.append(lights[row_idx+1][col_idx+1])
    if col_idx < len(lights[0])-1:
        # R
        neighbors.append(lights[row_idx][col_idx+1])
    return sum(neighbors)



def main(lights, part_1: bool):
    if not part_1:
        corners = [(0, 0), (len(lights)-1, 0), (len(lights)-1, len(lights[0])-1), (0, len(lights[0])-1)]
        for corner in corners:
            lights[corner[0]][corner[1]] = True
    for _ in range(100):
        temp = deepcopy(lights)
        for row_idx in range(len(lights)):
            for col_idx in range(len(lights[0])):
                if not part_1 and (row_idx, col_idx) in corners:
                    continue
                if lights[row_idx][col_idx]:
                    if get_neighbors_that_are_on(lights, row_idx, col_idx) not in [2, 3]:
                        temp[row_idx][col_idx] = False
                else:
                    if get_neighbors_that_are_on(lights, row_idx, col_idx) == 3:
                        temp[row_idx][col_idx] = True
        lights = deepcopy(temp)
    return sum([sum(row) for row in lights])

print(f"Part 1: {main(make_lights(), True)}")
print(f"Part 2: {main(make_lights(), False)}")