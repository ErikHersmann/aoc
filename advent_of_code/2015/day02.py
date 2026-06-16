from helper import problem_data
from math import prod

sorted_sides = [sorted(map(int, line.split("x"))) for line in problem_data.splitlines()]
print(f"Part 1: {sum([3*l*w + 2*w*h + 2*h*l for l,w,h in sorted_sides])}")
print(f"Part 2: {sum([2*l + 2*w + (l*w*h) for l,w,h in sorted_sides])}")