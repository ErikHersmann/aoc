from helper import problem_data, is_integer_negative_support
from collections import defaultdict
# You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

# The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

#     set X Y sets register X to the value of Y.
#     sub X Y decreases register X by the value of Y.
#     mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
#     jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

#     Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

# The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

# If you run the program (your puzzle input), how many times is the mul instruction invoked?


registers = defaultdict(int)
registers["a"] = 1
pointer = 0
mul_invoked = 0
instructions = [line.split() for line in problem_data.splitlines()]
while pointer < len(instructions):
    print(registers, "\n")
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
print(mul_invoked)
print(registers["h"])

# If ran to completion what is the value in h