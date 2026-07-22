from helper import problem_data


registers = {"a": 0, "b": 0, "c": 1, "d": 0}
instructions = [line.split() for line in problem_data.splitlines()]
ptr = 0
while ptr < len(instructions):
    line = instructions[ptr]
    opcode = line[0]
    match opcode:
        case "cpy":
            assert len(line) == 3
            if line[1].isnumeric():
                registers[line[2]] = int(line[1])
            else:
                registers[line[2]] = registers[line[1]]
            ptr += 1
        case "inc":
            assert len(line) == 2
            registers[line[1]] += 1
            ptr += 1
        case "dec":
            assert len(line) == 2
            registers[line[1]] -= 1
            ptr += 1
        case "jnz":
            assert len(line) == 3
            if line[1].isnumeric():
                val = int(line[1])
            else:
                val = registers[line[1]]
            if val != 0:
                ptr += int(line[2])
            else:
                ptr += 1
        case "tgl":
            assert len(line) == 2
            
for register in registers:
    print(register, registers[register])