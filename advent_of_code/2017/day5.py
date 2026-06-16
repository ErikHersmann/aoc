from helper import problem_data

# TODO: Do this in a smart way by detecting cycles and arithmetically resolving them without simulation

# For our input data it is more than feasible to just brute force simulate all 1050 something lines because we have -1000 at most as an average of negative values
# meaning we execute at most a million operations which should be instant

instructions = [int(line.strip()) for line in problem_data.splitlines()]
pointer = 0
step = 0

while pointer < len(instructions):
    prev_pointer = pointer
    pointer += instructions[pointer]
    instructions[prev_pointer] += -1 if instructions[prev_pointer] >= 3 else 1
    step += 1
pass
print(step)