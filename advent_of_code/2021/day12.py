from helper import problem_data
from collections import defaultdict

# problem_data = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end
# """

lowercase = set()
choices = defaultdict(set)
for line in problem_data.splitlines():
    left, right = line.split("-")
    choices[left].add(right)
    choices[right].add(left)
    for i in [left, right]:
        if i == i.lower():
            lowercase.add(i)

# Find all unique paths that don't double a lowercase letter and go from start to end

paths = []
def part_1(path):
    if path[-1] == "end":
        paths.append(path)
        return
    for choice in choices[path[-1]]:
        if choice in lowercase and choice in path:
            continue
        else:
            temp = path[::] + [choice]
            part_1(temp)

part_1(["start"])
print(f"Part 1: {len(paths)}")

paths = []
def part_2(path, is_double):
    if path[-1] == "end":
        paths.append(path)
        return
    for choice in choices[path[-1]]:
        if choice == "start":
            continue
        if choice in lowercase and choice in path:
            if is_double:
                continue
            else:
                temp = path[::] + [choice]
                part_2(temp, True)
        else:
            temp = path[::] + [choice]
            part_2(temp, is_double)

part_2(["start"], False)
print(f"Part 2: {len(paths)}")