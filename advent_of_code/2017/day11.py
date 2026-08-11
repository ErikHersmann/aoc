from collections import defaultdict
from helper import problem_data, maxsize
from copy import deepcopy


def calculate(b):
    d = deepcopy(b)
    d["n"], d["s"] = max(0, d["n"]-d["s"]), max(0, d["s"]-d["n"])
    d["ne"], d["sw"] = max(0, d["ne"]-d["sw"]), max(0, d["sw"]-d["ne"])
    d["nw"], d["se"] = max(0, d["nw"]-d["se"]), max(0, d["se"]-d["nw"])
    d["n"] = max(0, d["n"]-d["se"])
    d["n"] = max(0, d["n"]-d["sw"])
    d["s"] = max(0, d["s"]-d["ne"])
    d["s"] = max(0, d["s"]-d["nw"])
    d["nw"] = max(0, d["nw"]-d["ne"])
    d["ne"] = max(0, d["ne"]-d["nw"])
    d["sw"] = max(0, d["sw"]-d["se"])
    d["se"] = max(0, d["se"]-d["sw"])
    return sum([val for val in d.values()])

xinitoro = defaultdict(int)
best = 0
for direction in problem_data.split(","):
    xinitoro[direction] += 1
    best = max(best, calculate(xinitoro))

print(f"Part 1: {calculate(xinitoro)}")
print(f"Part 2: {best}")