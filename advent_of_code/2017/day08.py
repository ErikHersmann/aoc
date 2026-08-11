from helper import problem_data
from collections import defaultdict
from sys import maxsize

registers = defaultdict(int)
best = -maxsize
for line in problem_data.splitlines():
    target_reg, op, amount, _, compare_reg, compare_op, compare_value = line.split()
    registers[target_reg] += (int(amount) * (-1 if op == "dec" else 1)) if eval(f"registers[\"{compare_reg}\"] {compare_op} {compare_value}") else 0
    best = max(best, registers[target_reg])

print(f"Part 1: {max([value for value in registers.values()])}")
print(f"Part 2: {best}")