from helper import problem_data

instructions = [line.replace(",", "").split() for line in problem_data.splitlines()]
PART = 2
registers = {"a": 0 if PART == 1 else 1, "b": 0}

instruction_pointer = 0
while instruction_pointer < len(instructions):
    current_instruction = instructions[instruction_pointer]
    match  current_instruction[0]:
        case "hlf":
            registers[current_instruction[1]] //= 2
            instruction_pointer += 1
            continue
        case "tpl":
            registers[current_instruction[1]] *= 3
            instruction_pointer += 1
            continue
        case "inc":
            registers[current_instruction[1]] += 1
            instruction_pointer += 1
            continue
        case "jmp":
            instruction_pointer += int(current_instruction[1])
            continue
        case "jie":
            if registers[current_instruction[1]] % 2 == 0:
                instruction_pointer += int(current_instruction[2])
            else:
                instruction_pointer += 1
            continue
        case "jio":
            if registers[current_instruction[1]] == 1:
                instruction_pointer += int(current_instruction[2])
            else:
                instruction_pointer += 1
            continue
print(f"part {PART}: {registers['b']}")