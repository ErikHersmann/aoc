from helper import problem_data
from copy import deepcopy

containers = sorted([int(line) for line in problem_data.splitlines()], reverse=True)

# DP
# Either skip current (move pointer)
# Or add current to total (move pointer)
valids = []
# TODO: Instead of path just track count of added indices
def dfs(index, total, path):
    global valids
    if index >= len(containers) or total > 150:
        return
    total_if_add = containers[index] + total
    copy = deepcopy(path)
    copy.append(index)
    if total_if_add == 150:
        valids.append(copy)
    dfs(index + 1, total_if_add, copy)
    dfs(index + 1, total, deepcopy(path))
dfs(0, 0, [])
lengths = {}
for l in sorted(valids, key=lambda x: len(x)):
    if len(l) not in lengths:
        lengths[len(l)] = 0
    lengths[len(l)] += 1
print(lengths)
# 555 too low
