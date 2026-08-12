from enum import Enum
from collections import defaultdict


class State(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6

state = State.A
terminate_after = 12523873
tape = defaultdict(int)
position = 0
iteration = 0

while iteration < terminate_after:
    match state:
        case State.A:
            if not tape[position]:
                tape[position] = 1
                position += 1
                state = State.B
            else:
                tape[position] = 1
                position -= 1
                state = State.E
        case State.B:
            state = State.F if tape[position] else State.C
            tape[position] = 1
            position += 1
        case State.C:
            if not tape[position]:
                state = State.D
                tape[position] = 1
                position -= 1
            else:
                state = State.B
                tape[position] = 0
                position += 1
        case State.D:
            if not tape[position]:
                state = State.E
                tape[position] = 1
                position += 1
            else:
                state = State.C
                tape[position] = 0
                position -= 1
        case State.E:
            if not tape[position]:
                state = State.A
                tape[position] = 1
                position -= 1
            else:
                state = State.D
                tape[position] = 0
                position += 1
        case State.F:
            state = State.C if tape[position] else State.A
            tape[position] = 1
            position += 1
    iteration += 1

print(sum([val for val in tape.values()]))










