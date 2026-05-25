from helper import problem_data
from collections import defaultdict

def parse_marker(line, pointer):
    assert line[pointer] == "("
    pointer += 1
    scope = ""
    multiplier = ""
    while line[pointer] != "x":
        assert line[pointer].isnumeric()
        scope += line[pointer]
        pointer += 1
    assert line[pointer] == "x"
    pointer += 1
    while line[pointer] != ")":
        assert line[pointer].isnumeric()
        multiplier += line[pointer]
        pointer += 1
    assert line[pointer] == ")"
    return int(scope), int(multiplier), pointer

def calculate_line_length(line: str):
    line_length = 0
    pointer = 0
    char_multiplier = 1
    scopes = defaultdict(list)
    while pointer < len(line):
        if line[pointer] == "(":
            scope, mult, pointer = parse_marker(line, pointer)
            scopes[pointer+scope].append(mult)
            char_multiplier *= mult
        elif line[pointer].isalpha():
            line_length += char_multiplier
        pointer += 1
        for scope in scopes:
            if scope < pointer:
                while len(scopes[scope]) > 0:
                    mult = scopes[scope].pop(0)
                    char_multiplier //= mult
    return line_length

print(sum([calculate_line_length(line) for line in problem_data.splitlines()]))