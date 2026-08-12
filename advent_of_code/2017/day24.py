from helper import problem_data
from copy import deepcopy
from sys import setrecursionlimit

setrecursionlimit(10**6)
components = set([tuple(map(int, line.split("/"))) for line in problem_data.splitlines()])
best = [0]

def dp (unvisited, next_port, strength):
    cpy = deepcopy(components)
    for component in unvisited:
        if next_port in component:
            cpy = deepcopy(components)
            cpy.remove(component)
            dp(cpy, component[(component.index(next_port)+1)%2] , sum(component))
    if strength > best[0]:
        best[0] = strength

for component in components:
    if 0 in component:
        cpy = deepcopy(components)
        cpy.remove(component)
        dp(cpy, [x for x in component if x != 0][0], sum(component))

# Greedy-ish search
# If we prio the "heavy" nodes first, the first path we find is already the heaviest ?

print(best[0])