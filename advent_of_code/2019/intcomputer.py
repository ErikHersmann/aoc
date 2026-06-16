from helper import day2_data, day5_data, day9_data
from math import prod
from collections import defaultdict

def main(data: str, input_number: int):
    valid_opcodes = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 99])
    registers = defaultdict()
    for pointer_2, x in enumerate(data.split(",")):
        registers[pointer_2] = int(x)
    pointer = 0
    RELATIVE_BASE = 0
    outputs = []

    def get_arguments(pointer: int, count: int):
        arguments = []
        modes = [int(x) for x in ((str(registers[pointer])[:-2]).zfill(count))[::-1]]
        for offset in range(count):
            match modes[offset]:
                case 0:
                    # Position
                    arguments.append(registers.get(registers.get(pointer + 1 + offset)))
                case 1:
                    # Immediate
                    arguments.append(registers.get(pointer + 1 + offset))
                case 2:
                    # Relative
                    raise NotImplementedError()
        return arguments

    while registers[pointer] != 99:
        opcode = int(str(registers[pointer])[-2:])
        assert opcode in valid_opcodes, f"opcode not valid: {opcode}"
        match opcode:
            case 1 | 2:
                # + and *
                output_ptr = registers[pointer + 3]
                arguments = get_arguments(pointer, 2)
                registers[output_ptr] = (
                    sum(arguments) if opcode == 1 else prod(arguments)
                )
                pointer += 4
            case 3:
                # Input
                # TODO: Fix this
                registers[registers[pointer + 1]] = input_number
                pointer += 2
            case 4:
                # Output
                # TODO: Fix this
                value = registers[registers[pointer + 1]]
                print(value)
                outputs.append(value)
                pointer += 2
            case 5 | 6:
                # jump
                arguments = get_arguments(pointer, 2)
                if (arguments[0] != 0 and opcode == 5) or (
                    arguments[0] == 0 and opcode == 6
                ):
                    pointer = arguments[1]
                else:
                    pointer += 3
            case 7 | 8:
                arguments = get_arguments(pointer, 2)
                output_ptr = registers[pointer + 3]
                registers[output_ptr] = (
                    int(arguments[0] < arguments[1])
                    if opcode == 7
                    else int(arguments[0] == arguments[1])
                )
                pointer += 4
            # case 9:
            #     RELATIVE_BASE += arguments[0]
            #     pointer += 2
    return {"day2": registers[0], "day5": outputs[-1] if len(outputs) > 0 else 0, "day9": 0}


datas = [day2_data, day5_data, day9_data]
expecteds = [779478, 2140710, 0]
keys = ["day2", "day5", "day9"]
inputs = [0, 5, 1]
for key, data, expected, inp in zip(keys, datas, expecteds, inputs):
    if key == "day2": continue
    test_value = main(data, inp)
    assert (
        test_value[key] == expected
    ), f"({key}) Expected {expected} but got {test_value[key]}"
