from helper import problem_data

print(f"Part 1: {(heights:= [prev:= 0] and [(prev:= (1 if current == "(" else -1) + prev) for current in problem_data])[-1]}")
print(f"Part 2: {heights.index(-1)+1}")
