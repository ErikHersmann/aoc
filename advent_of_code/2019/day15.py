from helper import problem_data
from math import prod
from collections import defaultdict
from enum import Enum
from os import system
from getch import getch
import json
from sys import argv
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
RELATIVE_OFFSET = 0
VIDEO_MAP = defaultdict(int)
MAX_ROW = 0
MAX_COL = 0
MIN_ROW = 0
MIN_COL = 0
CURRENT_POSITION = (0, 0)
last_input, last_output = None, None
FOUND = False
LAST_GEN_OXYGENS = []


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
    assert val in [0, 2], f"Output pointer parameter mode should be "
    return ParameterMode(val)


def draw():
    system("clear")
    print(
        "     "
        + " ".join([str(i).zfill(5) for i in range(MIN_COL, MAX_COL + 1) if i % 5 == 0])
    )
    for row in range(MIN_ROW, MAX_ROW + 1):
        print(str(row).zfill(5), end=" ")
        for col in range(MIN_COL, MAX_COL + 1):
            key = (row, col)
            if key == (CURRENT_POSITION[1], CURRENT_POSITION[0]):
                print("🟨", end="")
                continue
            if key not in VIDEO_MAP:
                print("🔲", end="")
                continue
            match VIDEO_MAP[key]:
                case 0:
                    print("⬛", end="")
                case 1:
                    print("🟦", end="")
                case 2:
                    cprint("🟩", end="", color="light_green")
        print()
    print(
        f"Width: {MAX_COL-MIN_COL} | Height: {MAX_ROW-MIN_ROW} | Position: {CURRENT_POSITION} | Moves: {counter} | Oxygen Turns: {oxygen_counter}"
    )


def get_mapped_input():
    global last_input, last_output
    # val = getch()
    val = getch()
    auto = val == "q"
    if auto:
        choices_list = ["w", "s", "a", "d"]
        weights = [0.25 for _ in range(4)]
        if last_input and last_output:
            if last_output == 1:
                weights[last_input - 1] * 3
            else:
                weights[last_input - 1] = 0
        val = choices(choices_list, weights=weights, k=1)[0]
    match val:
        case "w":
            return 1
        case "a":
            return 3
        case "s":
            return 2
        case "d":
            return 4
    raise Exception("Unreachable?")


def transform_current_position(last_input: int, forward: bool):
    global CURRENT_POSITION
    mult = 1 if forward else -1
    match last_input:
        case 1:
            CURRENT_POSITION = (CURRENT_POSITION[0], CURRENT_POSITION[1] + (mult * -1))
        case 3:
            CURRENT_POSITION = (CURRENT_POSITION[0] + (mult * -1), CURRENT_POSITION[1])
        case 2:
            CURRENT_POSITION = (CURRENT_POSITION[0], CURRENT_POSITION[1] + (mult * 1))
        case 4:
            CURRENT_POSITION = (CURRENT_POSITION[0] + (mult * 1), CURRENT_POSITION[1])


def get_neighbors(position: tuple):
    return [
        (position[0] + 1, position[1]),
        (position[0] - 1, position[1]),
        (position[0], position[1] + 1),
        (position[0], position[1] - 1),
    ]


def spread_oxygen():
    global VIDEO_MAP, oxygen_counter, LAST_GEN_OXYGENS
    oxygen_counter += 1
    temp = set()
    for pos in LAST_GEN_OXYGENS:
        for neighbor in get_neighbors(pos):
            if neighbor in VIDEO_MAP and VIDEO_MAP[neighbor] == 1:
                VIDEO_MAP[neighbor] = 2
                temp.add(neighbor)
    LAST_GEN_OXYGENS = list(temp)


counter = 0
oxygen_counter = 0
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
                counter += 1
                last_input = get_mapped_input()
                transform_current_position(last_input, True)
                MAX_ROW = max(MAX_ROW, CURRENT_POSITION[1])
                MIN_ROW = min(MIN_ROW, CURRENT_POSITION[1])
                MAX_COL = max(MAX_COL, CURRENT_POSITION[0])
                MIN_COL = min(MIN_COL, CURRENT_POSITION[0])
                registers[get_output_pointer(pointer, 1)] = last_input
                if FOUND:
                    spread_oxygen()
            else:
                last_output = get_arguments(pointer, 1)[0]
                key = (CURRENT_POSITION[1], CURRENT_POSITION[0])
                if key not in VIDEO_MAP:
                    VIDEO_MAP[key] = last_output
                if last_output == 0:
                    transform_current_position(last_input, False)
                if last_output == 2:
                    FOUND = True
                    LAST_GEN_OXYGENS.append(key)
                draw()
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
