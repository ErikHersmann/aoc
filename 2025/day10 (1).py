from helper import short_test, input_data
from sys import maxsize

res2 = 0
data = input_data

data = [y.split() for y in data.splitlines()]
for idx, line in enumerate(data):
    goal, buttons, goal_2 = line[0], line[1:-1], line[-1]
    goal = [1 if val == "#" else 0 for val in goal[1:-1]]
    goal_2 = [int(x) for x in goal_2[1:-1].split(",")]
    buttons = sorted([[int(x) for x in (val[1:-1]).split(",")] for val in buttons], key= lambda x: len(x), reverse=True)
    initial_state = [0 for _ in range(len(goal))]
    best = [maxsize]
    visited = {}
    max_times_each = [min([goal_2[number] for number in button]) for button in buttons]
    # Starting position should be determined by combining all buttons so you can press any button without overflowing
    # Dp too expensive for part 2
    # Find maximum state so that you can still press all buttons

print(res2)

