from helper import problem_data
from collections import defaultdict
from sys import setrecursionlimit, maxsize

setrecursionlimit(100000)

graph, target = problem_data.split("\n\n")

forward_dict = defaultdict(set)
backward_dict = {}
for lin in graph.splitlines():
    l, r = lin.split(" => ")
    forward_dict[l].add(r)
    backward_dict[r] = l

cache = defaultdict(lambda: maxsize)
cache_2 = {}


def dp(remaining_target: str, pointer: int, steps: int):
    if (
        pointer >= len(remaining_target)
        or cache["e"] <= steps
        or cache[remaining_target] < steps
    ):
        return
    cache[remaining_target] = steps
    if remaining_target == "e":
        print(steps)
    key = (remaining_target, pointer)
    if key not in cache_2:
        cache_2[key] = steps
    elif cache_2[key] <= steps:
        return
    # Replace pointer of remaining_target with all possibilities
    for offset in range(1, min(11, len(remaining_target) - pointer + 1)):
        if (substring := remaining_target[pointer : pointer + offset]) in backward_dict:
            dp(
                remaining_target[:pointer]
                + backward_dict[substring]
                + remaining_target[pointer + offset :],
                0,
                steps + 1,
            )
        dp(
            remaining_target,
            pointer + offset,
            steps,
        )

# We get the correct result but don't terminate ehm
dp(target, 0, 0)
