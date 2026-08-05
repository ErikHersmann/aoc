from helper import problem_data
from collections import deque

# Find any valid path through the graph given in problem_data
problem_data = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

l = []
no_deps = set()
has_deps = set()
deps = [[element for index, element in enumerate(line.split()) if index in [1, 7]] for line in problem_data.splitlines()]
n = set()
for left, right in deps:
    n.add(left)
    n.add(right)
n = len(n)
while len(l) < n:
    for left, right in deps:
        if left in l:
            no_deps.add(right)
            continue
        if right in no_deps:
            no_deps.remove(right)
        if left not in no_deps and left not in has_deps:
            no_deps.add(left)
        has_deps.add(right)
    l.extend(sorted([x for x in no_deps if x not in l]))
print("".join(l))
# Make a full pass and append all the ones that don´t have a dependency to a deque
# CABDFE