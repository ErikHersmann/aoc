from helper import problem_data
from time import sleep
from copy import deepcopy

problem_data = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

x_bounds = [0, 0]
y_bounds = [0, 0]
positions = {}
velocities = {}
for id_, line in enumerate(problem_data.splitlines()):
    line = line.split("> velocity=<")
    pos = tuple(int(x) for x in line[0].strip("position=<").split(","))
    velocity = tuple(int(x) for x in line[1].strip(">").split(","))
    positions[pos] = id_
    velocities[id_] = velocity
    x_bounds = [min(x_bounds[0], pos[0]), max(x_bounds[1], pos[0])]
    y_bounds = [min(y_bounds[0], pos[1]), max(y_bounds[1], pos[1])]

t = 0
while True:
    temp = {}
    temp_x_bounds = x_bounds
    temp_y_bounds = y_bounds
    for x in range(x_bounds[0] - 1, x_bounds[1] + 1):
        for y in range(y_bounds[0] - 1, y_bounds[1] + 1):
            if (x, y) in positions:
                print("#", end="")
                id_ = positions.pop((x, y))
                vel = velocities[id_]
                new_position = (x + vel[0], y + vel[1])
                temp_x_bounds = [
                    min(x_bounds[0], new_position[0]),
                    max(x_bounds[1], new_position[0]),
                ]
                temp_y_bounds = [
                    min(y_bounds[0], new_position[1]),
                    max(y_bounds[1], new_position[1]),
                ]
                if new_position not in temp:
                    temp[new_position] = []
                temp[new_position].append(id_)
            else:
                print(".", end="")
        print()
    print("\n\n")
    positions = deepcopy(temp)
    x_bounds = temp_x_bounds
    y_bounds = temp_y_bounds
    t += 1
    sleep(0.8)
