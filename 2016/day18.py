from helper import throw

def main(part_1: bool):
    problem_data = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"
    width = len(problem_data)
    # Its left and center tiles are traps, but its right tile is not.
    a = "^^."
    # Its center and right tiles are traps, but its left tile is not.
    b = ".^^"
    # Only its left tile is a trap.
    c = "^.."
    # Only its right tile is a trap.
    d = "..^"
    cases = [a, b, c, d]

    ROWS = 400000 if not part_1 else 40
    safe_tiles = sum([1 for c in problem_data if c == "."])
    graph = [[c for c in problem_data]]
    for row in range(1, ROWS):
        graph.append([])
        for col_idx in range(width):
            neighbor_string = ""
            neighbor_string += graph[-2][col_idx-1] if col_idx > 0 else "."
            neighbor_string += graph[-2][col_idx]
            neighbor_string += graph[-2][col_idx+1] if col_idx < width -1 else "."
            tile = "." if neighbor_string not in cases else "^"
            safe_tiles += 1 if tile == "." else 0
            graph[-1].append(tile)
    return safe_tiles
print(f"Part 1: {main(True)}")
print(f"Part 2: {main(False)}")
# Cache for part 2: but w/e hardware carries
# And discard old rows, we only need to keep track of 2 rows at most at any given time