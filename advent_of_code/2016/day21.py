from helper import problem_data, throw
from itertools import permutations


def scramble(password: str):
    password = [c for c in password]
    for line in problem_data.splitlines():
        line = line.split()
        op = " ".join(line[:2])
        match op:
            case "swap position":
                x, y = map(int, [line[2], line[-1]])
                password[x], password[y] = password[y], password[x]
            case "swap letter":
                letter_a, letter_b = line[2], line[-1]
                x, y = password.index(letter_a), password.index(letter_b)
                password[x], password[y] = password[y], password[x]
            case "rotate right":
                x = int(line[2])
                password = password[-x:] + password[:-x]
            case "rotate left":
                x = int(line[2])
                password = password[x:] + password[:x]
            case "rotate based":
                letter_a = line[-1]
                x = (
                    password.index(letter_a)
                    + 1
                    + (1 if password.index(letter_a) >= 4 else 0)
                ) % len(password)
                password = password[-x:] + password[:-x]
            case "reverse positions":
                x, y = map(int, [line[2], line[-1]])
                y += 1
                password = password[:x] + password[x:y][::-1] + password[y:]
            case "move position":
                x, y = map(int, [line[2], line[-1]])
                password.insert(y, password.pop(x))
            case default:
                throw()
    return "".join(password)


print(f"Part 1: {scramble("abcdefgh")}")
for perm in permutations([c for c in "fbgdceah"], len("fbgdceah")):
    if scramble(perm) == "fbgdceah":
        print(f"Part 2: {''.join(perm)}")
