from helper import problem_data, throw
from math import prod
from collections import defaultdict
from enum import Enum
from os import system
from termcolor import cprint
from random import choices

data = problem_data


class ParameterMode(Enum):

    Position = 0

    Immediate = 1

    Relative = 2


valid_opcodes = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 99])
valid_parameter_modes = set([0, 1, 2])
registers = defaultdict()
for pointer_2, x in enumerate(data.split(",")):
    registers[pointer_2] = int(x)
pointer = 0
# registers[0] = 2
RELATIVE_OFFSET = 0
VIDEO_MAP = defaultdict(int)
MAX_ROW = 0
MAX_COL = 0
MIN_ROW = 0
MIN_COL = 0
CURRENT_POSITION = (0, 0)
last_input, last_output = None, None
FOUND = False
MAP = [[]]
main_string = [ord(x) for x in "B,B,A,C,C,B,A,C,B,A"]
sub_a = [ord(x) for x in "L,8,L,8,R,12,L,8,L,8"]
sub_b = [ord(x) for x in "L,12,L,12,R,12"]
sub_c = [ord(x) for x in "L,10,R,8,R,12"]
INPUT_STACK = []
INPUT_STACK.extend(main_string)
INPUT_STACK.append(ord("\n"))
INPUT_STACK.extend(sub_a)
INPUT_STACK.append(ord("\n"))
INPUT_STACK.extend(sub_b)
INPUT_STACK.append(ord("\n"))
INPUT_STACK.extend(sub_c)
INPUT_STACK.append(ord("\n"))
INPUT_STACK.append(ord("y"))
INPUT_STACK.append(ord("\n"))
registers[0] = 2


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
        return registers[pointer + distance] + RELATIVE_OFFSET
    return registers[pointer + distance]


def get_output_parameter_mode(pointer: int, distance: int):
    val = int(str(registers[pointer])[:-2].zfill(distance)[0])
    assert val in [0, 2], f"Output pointer parameter mode should be 0 or 2"
    return ParameterMode(val)


def get_neighbors(position: tuple):
    return [
        (position[0] + 1, position[1]),
        (position[0] - 1, position[1]),
        (position[0], position[1] + 1),
        (position[0], position[1] - 1),
    ]


print("    " + " ".join([str(i).zfill(2) for i in range(50) if i % 3 == 0]))
print("000 ", end="")
row_counter = 0
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
                assert len(INPUT_STACK) > 0
                inp = INPUT_STACK.pop(0)
                registers[get_output_pointer(pointer, 1)] = inp
            else:
                last_output = get_arguments(pointer, 1)[0]
                if last_output > 1000:
                    print(last_output)
                    exit(0)
                print(chr(last_output), end="")
                if last_output == 10:
                    row_counter += 1
                    print(str(row_counter).zfill(3), end=" ")
                    MAP.append([])
                else:
                    MAP[-1].append(chr(last_output))
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

# TODO: Move to green position with all of the map discovered
# Keep a counter of moves from that point onward and change the value of that in the video map to 2 if it is one
# For each timeste change all neighbors of an active 2 (last timestep new 2s) to 2 if they are blue else skip
# Disable random input if the first 2 is found

def draw_map():
    print()
    res1 = 0
    for row in range(1, len(MAP) - 3):
        for col in range(1, len(MAP[0]) - 1):
            if MAP[row][col] == "^":
                start = (row, col)
            if (
                MAP[row - 1][col] == "#"
                and MAP[row + 1][col] == "#"
                and MAP[row][col + 1] == "#"
                and MAP[row][col - 1] == "#"
            ):
                res1 += row * col


def add(pos1: tuple, pos2: tuple):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def access_map(pos: tuple):
    return MAP[pos[0]][pos[1]]


def oob(pos: tuple):
    (row, col) = pos
    H, W = len(MAP), len(MAP[0])
    return row < 0 or col < 0 or row > H - 3 or col > W - 1


def get_program():
    UP, LEFT, RIGHT, DOWN = (-1, 0), (0, -1), (0, 1), (1, 0)
    LEFT_MAP = {UP: LEFT, LEFT: DOWN, DOWN: RIGHT, RIGHT: UP}
    RIGHT_MAP = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}
    REVERSE_MAP = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
    INSTRUCTIONS = []
    DIRECTION = UP
    LINE_LENGTH = 0
    next = add(start, DIRECTION)
    TARGET = (8, 24)
    while start != TARGET:
        while access_map(next) == "#":
            LINE_LENGTH += 1
            next = add(next, DIRECTION)
            if oob(next):
                break
        start = add(next, REVERSE_MAP[DIRECTION])
        print(start)
        if start == TARGET:
            INSTRUCTIONS.pop(0)
            INSTRUCTIONS.append(str(LINE_LENGTH))
            sinst = ",".join(INSTRUCTIONS)
            print(sinst)
            break
        INSTRUCTIONS.append(str(LINE_LENGTH))
        LINE_LENGTH = 0
        if access_map(add(start, LEFT_MAP[DIRECTION])) == "#":
            INSTRUCTIONS.append("L")
            DIRECTION = LEFT_MAP[DIRECTION]
        elif access_map(add(start, RIGHT_MAP[DIRECTION])) == "#":
            INSTRUCTIONS.append("R")
            DIRECTION = RIGHT_MAP[DIRECTION]
        else:
            throw()
        next = add(start, DIRECTION)


def compress_program():
    inst_1 = INSTRUCTIONS
    sinst_1 = sinst
    # A
    for SEGMENT_LENGTH_1 in range(10, -1, -1):
        for idx_1 in range(0, len(inst_1)):
            segment = ",".join(inst_1[idx_1:idx_1+SEGMENT_LENGTH_1])
            if len(segment) < 21:
                A_VALUE = segment
                sinst_2 = sinst_1.replace(A_VALUE, "A")
                inst_2 = sinst_2.split(",")

                # B
                for SEGMENT_LENGTH_2 in range(10, -1, -1):
                    for idx_2 in range(0, len(inst_2)):
                        segment = ",".join(inst_2[idx_2:idx_2+SEGMENT_LENGTH_2])
                        if len(segment) < 21 and "A" not in segment:
                            B_VALUE = segment
                            sinst_3 = sinst_2.replace(B_VALUE, "B")
                            inst_3 = sinst_3.split(",")

                            # C
                            for SEGMENT_LENGTH_3 in range(10, -1, -1):
                                for idx_3 in range(0, len(inst_3)):
                                    segment = ",".join(inst_3[idx_3:idx_3+SEGMENT_LENGTH_3])
                                    if len(segment) < 21 and "A" not in segment and "B" not in segment:
                                        C_VALUE = segment
                                        sinst_4 = sinst_3.replace(C_VALUE, "C")

                                        # Result
                                        if len(sinst_4) < 21:
                                            print(f"Length of segments: {str(len(A_VALUE)).ljust(3)} {str(len(B_VALUE)).ljust(3)} {str(len(C_VALUE)).ljust(3)} | {len(inst_1)}")
                                            print(
                                                f"A={A_VALUE.ljust(23)}B={B_VALUE.ljust(23)}C={C_VALUE.ljust(23)}\t({len(sinst_4)})\t{sinst_4}"
                                            )
                                            exit(0)
