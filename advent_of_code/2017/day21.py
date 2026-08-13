from helper import (
    problem_data,
    flip_square_string_90_degrees_right,
    flip_square_string_180_degrees_along_horizontal_axis,
    flip_square_string_180_degrees_along_vertical_axis,
)
from math import sqrt

pattern = """.#.
..#
###
"""
def deconstruct(string: str, target_size: int):
    rows = string.splitlines()
    chunks = []
    for row_idx in range(0, len(rows), target_size):
        for col_idx in range(0, len(rows[0]), target_size):
            chunk = []
            for i in range(target_size):
                chunk.append(rows[row_idx + i][col_idx : col_idx + target_size])
            chunk = "\n".join(chunk)
            chunks.append(chunk)
    return chunks


def stitch(list_of_squares):
    side_length = int(sqrt(len(list_of_squares)))
    square_length = len(list_of_squares[0].splitlines())
    output = []
    for idx, square in enumerate(list_of_squares):
        y = square_length * (idx // side_length)
        for line_idx, line in enumerate(square.splitlines()):
            if len(output) <= y + line_idx:
                output.append("")
            output[y + line_idx] += line
    return "\n".join(output)


enhancements = {}
for line in problem_data.splitlines():
    before, after = line.replace("/", "\n").split(" => ")
    enhancements[before] = after
    enhancements[flip_square_string_180_degrees_along_horizontal_axis(before)] = after
    enhancements[flip_square_string_180_degrees_along_vertical_axis(before)] = after
    for _ in range(3):
        before = flip_square_string_90_degrees_right(before)
        enhancements[before] = after
    before_h_flip = flip_square_string_180_degrees_along_horizontal_axis(before)
    for _ in range(3):
        before_h_flip = flip_square_string_90_degrees_right(before_h_flip)
        enhancements[before_h_flip] = after
    before_v_flip = flip_square_string_180_degrees_along_vertical_axis(before)
    for _ in range(3):
        before_v_flip = flip_square_string_90_degrees_right(before_v_flip)
        enhancements[before_v_flip] = after

iteration = 0
while iteration < 18:
    if len(pattern.splitlines()[0]) % 2:
        chunks = deconstruct(pattern, 3)
        chunks = [enhancements[chunk] for chunk in chunks]
        pattern = stitch(chunks)
    else:
        chunks = deconstruct(pattern, 2)
        chunks = [enhancements[chunk] for chunk in chunks]
        pattern = stitch(chunks)  
    iteration += 1
    if iteration == 5:
        print(f"Part 1: {pattern.count("#")}")

print(f"Part 2: {pattern.count("#")}")
