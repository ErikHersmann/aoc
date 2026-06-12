from helper import problem_data
from collections import defaultdict

d = defaultdict(set)
graph, target = problem_data.split("\n\n")
for assignment in graph.splitlines():
    l, r = assignment.split(" => ")
    d[l].add(r)


# we always grow so once we are length of target or larger exit recursion
cur = "e"