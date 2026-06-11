from helper import problem_data
from math import prod

# problem_data = """0: 3
# 1: 2
# 4: 4
# 6: 4"""
part_1 = sum([prod(nums) for line in problem_data.splitlines() if not (nums:= list(map(int, line.split(": "))))[0]%(2*nums[1]-2)])
inp = [((tupl:= tuple(map(int, line.split(": "))))[0], (2 * tupl[1] - 2)) for line in problem_data.splitlines()]
c = 0
while any(not (tup[0] + c) % tup[1] for tup in inp):
    c += 1

print(c)
