from helper import input_data, short_test
from math import dist, prod

res1 = 0

data = short_test
data = [[int(y) for y in x.split(",")] for x in data.splitlines()]
pass
n = len(data)
distances = []
# Calculate pairwise distances ?
for idx1 in range(n):
    for idx2 in range(idx1+1, n):
        distances.append([dist(data[idx1], data[idx2]), idx1, idx2])
distances.sort(reverse=False, key=lambda x: x[0])

sets = []
visited = {}
CONNECTIONS = 11
for _, idx1, idx2 in distances[:CONNECTIONS]:
    if idx1 in visited and idx2 in visited: continue
    if idx1 in visited and idx2 not in visited:
        sets[visited[idx1]].add(idx2)
        visited[idx2] = visited[idx1]
        continue
    if idx2 in visited and idx1 not in visited:
        sets[visited[idx2]].add(idx1)
        visited[idx1] = visited[idx2]
        continue
    assert idx1 not in visited and idx2 not in visited
    sets.append(set())
    set_idx = len(sets)-1
    visited[idx1] = set_idx
    visited[idx2] = set_idx
    sets[set_idx].add(idx1)
    sets[set_idx].add(idx2)
pass

