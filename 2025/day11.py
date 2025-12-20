from collections import defaultdict, deque
from helper import input_data, short_test
from copy import deepcopy as dc

data = short_test

map = defaultdict(set)

for line in data.splitlines():
    key, vals = line.split(":")
    map[key] = set(vals.split())
    pass

res1 = 0
q = deque(map["svr"])
paths = deque([["svr"]])
visited = set()

while len(q) > 0 and len(paths) > 0:
    current = q.popleft()
    path = paths.popleft()
    key = "_".join(path)
    if key in visited:
        continue
    visited.add(key)
    # if "out" in map[current]:
    #     res1 += 1
    #     continue
    for neighbor in map[current]:
        q.append(neighbor)
        new_path = dc(path)
        new_path.append(neighbor)
        paths.append(new_path)
    visited.add(current)

res1 = 0
res2 = set()
for val in visited:
    if val == "out":
        continue
    vals = val.split("_")
    if (
        # len(set(vals)) == len(vals)
        vals[-1] == "out"
        and "dac" in vals
        and "fft" in vals
    ):
        res1 += 1
        print(val)
        temp = ""
        res2.add()
print(res1)
