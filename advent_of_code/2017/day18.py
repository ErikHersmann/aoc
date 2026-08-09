from helper import problem_data, is_integer_negative_support
from copy import deepcopy
from collections import defaultdict, deque
# problem_data = """snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d"""
instructions = problem_data.splitlines()
send_count = [0, 0]

def run_program(index, program_registers, instruction_pointers, messages):
    instruction_pointer = instruction_pointers[index]
    registers = program_registers[index]
    while instruction_pointer < len(instructions):
        cur = instructions[instruction_pointer].split()
        match cur[0]:
            case "snd":
                arg = int(cur[1]) if is_integer_negative_support(cur[1]) else registers[cur[1]]
                messages[(index+1)%2].append(arg)
                send_count[index] += 1
                instruction_pointer += 1
                instruction_pointers[index] = instruction_pointer
                return 0
            case "set":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                registers[cur[1]] = arg
                instruction_pointer += 1
            case "add":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                if cur[1] not in registers:
                    registers[cur[1]] = 0
                registers[cur[1]] += arg
                instruction_pointer += 1
            case "mul":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                if cur[1] not in registers:
                    registers[cur[1]] = 0
                registers[cur[1]] *= arg
                instruction_pointer += 1
            case "mod":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                if cur[1] not in registers:
                    registers[cur[1]] = 0
                registers[cur[1]] %= arg
                instruction_pointer += 1
            case "rcv":
                if len(messages[index]) == 0:
                    instruction_pointers[index] = instruction_pointer
                    return 0
                registers[cur[1]] = messages[index].popleft()
                instruction_pointer += 1
            case "jgz":
                if cur[1] in registers and registers[cur[1]] > 0:
                    arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                    instruction_pointer += arg
                else:
                    instruction_pointer += 1
    return -1

program_registers = [{"p": 0}, {"p": 1}]
messages = [deque(), deque()]
instruction_pointers = [0, 0]

iteration = 0
# TODO: Doesn't terminate 
while True:
    if run_program(0, program_registers, instruction_pointers, messages) == -1:
        run_program(1, program_registers, instruction_pointers, messages)
        break
    elif run_program(1, program_registers, instruction_pointers, messages) == -1:
        run_program(0, program_registers, instruction_pointers, messages)
        break
    iteration += 1
    if not iteration%10**6:
        print(iteration, program_registers, send_count)
print(send_count)