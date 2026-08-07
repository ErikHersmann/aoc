from helper import problem_data
from collections import deque
from copy import deepcopy

# TODO: Very much in need of a refactoring


def part_1():
    solution = []
    deps = [
        [element for index, element in enumerate(line.split()) if index in [1, 7]]
        for line in problem_data.splitlines()
    ]
    unvisited = set()
    for left, right in deps:
        unvisited.add(left)
        unvisited.add(right)
    while len(unvisited) > 0:
        candidates = deepcopy(unvisited)
        for left, right in deps:
            if left in unvisited and right in candidates:
                candidates.remove(right)
        candidate = sorted(list(candidates))[0]
        unvisited.remove(candidate)
        solution.append(candidate)
    return "".join(solution)


def part_2():
    solution = []
    worker_count = 5
    workers = [0 for _ in range(worker_count)]
    tasks = ["" for _ in range(worker_count)]
    deps = [
        [element for index, element in enumerate(line.split()) if index in [1, 7]]
        for line in problem_data.splitlines()
    ]
    t = -1
    unvisited = set()
    for left, right in deps:
        unvisited.add(left)
        unvisited.add(right)
    while len(unvisited) > 0:
        for idx in range(worker_count):
            if workers[idx] > 1:
                workers[idx] -= 1
            elif workers[idx] == 1:
                workers[idx] = 0
                if tasks[idx] in unvisited:
                    unvisited.remove(tasks[idx])
                solution.append(candidate)
                tasks[idx] = ""
        candidates = deepcopy(unvisited)
        for left, right in deps:
            if left in unvisited and right in candidates:
                candidates.remove(right)
        candidates = [x for x in sorted(list(candidates)) if x not in tasks]
        for candidate in candidates:
            for idx in range(worker_count):
                if workers[idx] == 0:
                    workers[idx] += ord(candidate) - ord("A") + 61  # 61
                    tasks[idx] = candidate
                    break
        t += 1
    return t
