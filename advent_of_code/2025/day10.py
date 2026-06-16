from helper import short_test, input_data
from sys import maxsize

res1 = 0
data = input_data

data = [y.split() for y in data.splitlines()]
for line in data:
    goal, buttons, _ = line[0], line[1:-1], line[-1]
    goal = [1 if val == "#" else 0 for val in goal[1:-1]]
    buttons = [[int(x) for x in (val[1:-1]).split(",")] for val in buttons]
    initial_state = [0 for _ in range(len(goal))]
    best = [maxsize]
    visited = {}

    def dp(current: list, cost: int, prev_ops: list):
        key = "_".join([str(x) for x in sorted(prev_ops)])
        if key in visited and visited[key] <= cost:
            return
        visited[key] = cost
        if current == goal:
            best[0] = min(cost, best[0])
            return
        for idx, button in enumerate(buttons):
            # No double presses ?
            if idx in prev_ops:
                continue
            new = current[::]
            for number in button:
                new[number] += 1
                new[number] %= 2
            dp(new, cost + 1, [*prev_ops, idx])

    dp(initial_state, 0, [])
    res1 += best[0]
print(res1)

# DP the wiring to reach indicator state (convert that)
#
