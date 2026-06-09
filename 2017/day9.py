from helper import problem_data

# problem_data = """{{<!!>},{<!!>},{<!!>},{<!!>}}"""

curly_stack = 0
is_garbage = False

pointer = 0
score = 0
garbage_counter = 0
garbage_score = 0
while pointer < len(problem_data):
    character = problem_data[pointer]
    match character:
        case "{":
            if not is_garbage:
                curly_stack += 1
            else:
                garbage_score += 1
        case "}":
            if not is_garbage:
                score += curly_stack
                curly_stack -= 1
            else:
                garbage_score += 1
        case "!":
            pointer += 1 if is_garbage else 0
        case "<":
            if not is_garbage:
                is_garbage = True
            else:
                garbage_score += 1
        case ">":
            is_garbage = False
            garbage_score += garbage_counter
            garbage_counter = 0
        case _:
            if is_garbage:
                garbage_counter += 1
    pointer += 1
print(score)
print(garbage_score)