from functools import cache
from helper import input_data

map = {split_line[0]: split_line[1].split() for split_line in [line.split(":") for line in input_data.splitlines()]}

@cache
def dfs(cur, target, seen_1, seen_2):
    seen_1 |= cur == "dac"
    seen_2 |= cur == "fft"
    return seen_1 and seen_2 if cur == target else sum(dfs(neighbor, target, seen_1, seen_2) for neighbor in map[cur])