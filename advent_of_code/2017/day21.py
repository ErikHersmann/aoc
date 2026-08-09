from helper import problem_data, flip_square_string_90_degrees_right, flip_square_string_180_degrees_along_horizontal_axis, flip_square_string_180_degrees_along_vertical_axis
pattern  = """.#.
..#
###
"""

# man this is aids

def deconstruct(string: str, target_size: int):
    rows = string.splitlines()
    chunks = []
    for row_idx in range(0, len(rows), target_size):
        for col_idx in range(0, len(rows[0]), target_size):
            chunk = []
            for i in range(target_size):
                chunk.append(rows[row_idx+i][col_idx:col_idx+target_size])
            chunk = "\n".join(chunk)
            chunks.append(chunk)
    return chunks

def stitch(list_of_squares):
    pass

enhancements = {}
for line in problem_data.splitlines():
    before, after = line.replace("/", "\n").split(" => ")
    # 0 degrees
    enhancements[before] = after
    enhancements[flip_square_string_180_degrees_along_horizontal_axis(before)] = after
    enhancements[flip_square_string_180_degrees_along_vertical_axis(before)] = after
    # 90, 180, 270 degrees
    for _ in range(3):
        before = flip_square_string_90_degrees_right(before)
        enhancements[before] = after

pass
iteration = 0
size = 3
while iteration < 5:
    if not size%2:
        chunks = deconstruct(pattern, 2)
        chunks = [enhancements[chunk] for chunk in chunks]
        pattern = stitch(chunks)
    else:
        chunks = deconstruct(pattern, 3)
        chunks = [enhancements[chunk] for chunk in chunks]
        pattern = stitch(chunks)
    pass
# keep track of the size
# Rotate every rule 3x and add them to the dictionary
# After this just look at the size to determine how to split up
# Apply dictionary transformations and stitch back up
