from helper import problem_data, is_integer_negative_support
from collections import defaultdict
from time import sleep


registers = defaultdict(int)
pointer = 0
mul_invoked = 0
instructions = [line.split() for line in problem_data.splitlines()]
while pointer < len(instructions):
    inst = instructions[pointer]
    match inst[0]:
        case "set":
            registers[inst[1]] = int(inst[2]) if is_integer_negative_support(inst[2]) else registers[inst[2]]
            pointer += 1
        case "sub":
            registers[inst[1]] -= int(inst[2]) if is_integer_negative_support(inst[2]) else registers[inst[2]]
            pointer += 1
        case "mul":
            registers[inst[1]] *= int(inst[2]) if is_integer_negative_support(inst[2]) else registers[inst[2]]
            pointer += 1
            mul_invoked += 1
        case "jnz":
            if (0 != (int(inst[1]) if is_integer_negative_support(inst[1]) else registers[inst[1]])):
                pointer += int(inst[2]) if is_integer_negative_support(inst[2]) else registers[inst[2]]
            else:
                pointer += 1

print(f"Part 1: {mul_invoked}")

b = 109300
c = 126300
h = 0
while True:
    d = 2
    while d - b != 0:
        if (b/d).is_integer():
            h += 1
            break
        d += 1
    if b - c == 0:
        print(f"Part 2: {h}")
        break
    b += 17
