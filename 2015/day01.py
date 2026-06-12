from helper import problem_data

height = 0
first = None
for idx, c in enumerate(problem_data):
    height += 1 if c == "(" else -1
    if height == -1 and not first:
        first = f"Part 2: {idx+1}"
print(f"Part 1: {height}")
print(first)
