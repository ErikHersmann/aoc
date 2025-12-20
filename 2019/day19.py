from helper import problem_data
from math import prod
from collections import defaultdict
from enum import Enum
from os import system
from getch import getch
import json
from sys import argv
from termcolor import cprint

data = problem_data
INPUT_VALUE = 2


class ParameterMode(Enum):

    Position = 0

    Immediate = 1

    Relative = 2


valid_opcodes = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 99])
valid_parameter_modes = set([0, 1, 2])
registers = defaultdict()
for pointer_2, x in enumerate(data.split(",")):
    registers[pointer_2] = int(x)
registers[0] = 2
pointer = 0
RELATIVE_OFFSET = 0
VIDEO_MAP = defaultdict(int)
MAX_ROW = 0
MAX_COL = 0
VIDEO_BUFFER = []
SCORE = 0


def load_game():
    global MAX_ROW, MAX_COL
    output_reg = defaultdict(int)
    vid_map_2 = defaultdict(int)
    with open("save.json", "r") as f:
        regs = json.load(f)
        for key, val in regs.items():
            output_reg[int(key)] = int(val)
    with open("save_video.json", "r") as f:
        vid_map_1 = json.load(f)
        for key, val in vid_map_1.items():
            new_key = tuple([int(x) for x in key.replace("(", "").replace(")", "").split(",")])
            vid_map_2[
                new_key
            ] = int(val)
            MAX_COL = max(MAX_COL, new_key[1])
            MAX_ROW = max(MAX_ROW, new_key[0])
    with open("save_ptr.txt", "r") as f:
        ptr = int(f.read().strip())

    return output_reg, ptr, vid_map_2

def get_parameter_modes(pointer: int, count: int):
    parameter = (str(registers[pointer])[:-2]).zfill(count)
    modes = []
    for idx in range(len(parameter) - 1, len(parameter) - count - 1, -1):
        modes.append(ParameterMode(int(parameter[idx])))
    return modes


def get_arguments(pointer: int, count: int):
    modes = get_parameter_modes(pointer, count)
    pointer += 1
    arguments = []
    for offset, mode in enumerate(modes):
        match mode:
            case ParameterMode.Position:
                # Pointer after opcode
                access_pointer = registers[pointer + offset]
            case ParameterMode.Immediate:
                # Direct value after opcode
                access_pointer = pointer + offset
            case ParameterMode.Relative:
                # Pointer + Offset after opcode
                access_pointer = registers[pointer + offset] + RELATIVE_OFFSET
        assert access_pointer >= 0
        if access_pointer not in registers:
            registers[access_pointer] = 0
        arguments.append(registers[access_pointer])
    return arguments

def get_output_pointer(pointer: int, distance: int):
    if get_output_parameter_mode(pointer, distance) == ParameterMode.Relative:
        return registers[pointer+distance] + RELATIVE_OFFSET
    return registers[pointer+distance]

def get_output_parameter_mode(pointer: int, distance: int):
    val = int(str(registers[pointer])[:-2].zfill(distance)[0])
    assert val in [0, 2], f"Output pointer parameter mode should be "
    return ParameterMode(val)

def save_game(ptr: str):
    with open("save.json", "w") as f:
        json.dump(registers, f)
    with open("save_ptr.txt", "w") as f:
        f.write(ptr)
    with open("save_video.json", "w") as f:
        temp = {str(key): val for key, val in VIDEO_MAP.items()}
        json.dump(temp, f)

def draw():
    # system("cls")
    for row in range(MAX_ROW + 1):
        for col in range(MAX_COL + 1):
            match VIDEO_MAP[(row, col)]:
                case 0:
                    print(" ", end="")
                case 1:
                    print("#", end="")
                case 2:
                    print("8", end="")
                case 3:
                    print("_", end="")
                case 4:
                    cprint("O", end="", color="light_red")
        print()
    print(f"{'\n'*25}{SCORE}")

def get_mapped_input():
    val = getch()
    print(val)
    match val:
        case "a":
            return -1
        case "d":
            return 1
        case "s":
            return 0
        case "q":
            return 4
        case "w":
            return 5
        case "e":
            return 6
    raise Exception("Unreachable?")

def wrap_input(pointer: int):
    inp = get_mapped_input()
    match inp:
        case 4:
            save_game(str(pointer))
            print("Saved game!")
            return -1
        case 5:
            save_game(str(pointer))
            print("Saved game!")
            return 0
        case 6:
            save_game(str(pointer))
            print("Saved game!")
            return 1
    return inp


if len(argv) >=2 and argv[1].isnumeric() and int(argv[1]) == 1:
    registers, pointer, VIDEO_MAP = load_game()
counter = 0
while registers[pointer] != 99:
    opcode = int(str(registers[pointer])[-2:])
    assert opcode in valid_opcodes, f"opcode not valid: {registers[pointer]}"
    match opcode:
        case 1 | 2:
            # + and *
            output_pointer = get_output_pointer(pointer, 3)
            arguments = get_arguments(pointer, 2)
            registers[output_pointer] = (
                sum(arguments) if opcode == 1 else prod(arguments)
            )
            pointer += 4
        case 3 | 4:
            # I/O
            if opcode == 3:
                draw()
                inp = wrap_input(pointer)
                registers[get_output_pointer(pointer, 1)] = inp
            else:
                VIDEO_BUFFER.append(get_arguments(pointer, 1)[0])
                if len(VIDEO_BUFFER) == 3:
                    col = VIDEO_BUFFER.pop(0)
                    row = VIDEO_BUFFER.pop(0)
                    id = VIDEO_BUFFER.pop(0)
                    if col == -1 and row == 0:
                        SCORE = id
                    else:
                        VIDEO_MAP[(row, col)] = id
                        MAX_COL = max(MAX_COL, col)
                        MAX_ROW = max(MAX_ROW, row)
            pointer += 2
        case 5 | 6:
            # jump if != or ==
            arguments = get_arguments(pointer, 2)
            if (arguments[0] != 0 and opcode == 5) or (
                arguments[0] == 0 and opcode == 6
            ):
                pointer = arguments[1]
            else:
                pointer += 3
        case 7 | 8:
            # < and ==
            arguments = get_arguments(pointer, 2)
            registers[get_output_pointer(pointer, 3)] = (
                int(arguments[0] < arguments[1])
                if opcode == 7
                else int(arguments[0] == arguments[1])
            )
            pointer += 4
        case 9:
            # modify relative base
            arguments = get_arguments(pointer, 1)
            RELATIVE_OFFSET += arguments[0]
            pointer += 2
