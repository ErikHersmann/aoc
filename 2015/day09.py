from collections import defaultdict
from helper import problem_data


data = problem_data
data = [[parts[0], parts[2], int(parts[-1])] for line in data.splitlines() for parts in [line.split()]]
graph = {start: defaultdict(int) for start in {item for line in data for item in (line[0], line[1])}}
for start, end, dist in data:
    graph[start][end] = dist
    graph[end][start] = dist

parts = [float("inf"), -float("inf")]
def dfs(cost: int, cur: str, visited: set):
    global parts
    if len(visited) == len(graph):
        parts = [min(parts[0], cost), max(parts[1], cost)]
        return
    for neighbor, distance in [(n, d) for n, d in  graph[cur].items() if n not in visited]: dfs(cost+distance, neighbor, visited.union(set([neighbor])))

for start in graph:
    dfs(0, start, set([start]))

print(parts)
