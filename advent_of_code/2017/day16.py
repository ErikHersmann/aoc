from helper import *
from collections import defaultdict


def one_dance(programs, instructions):
    for instruction in instructions:
        match instruction[0]:
            case "s":
                size = int(instruction[1:])
                programs = programs[-size:] + programs[:-size]
            case "x":
                left, right = map(int, instruction[1:].split("/"))
                programs[left], programs[right] = programs[right], programs[left]
            case "p":
                left, right = instruction[1:].split("/")
                left, right = programs.index(left), programs.index(right)
                programs[left], programs[right] = programs[right], programs[left]
    return "".join(programs)

rank = 0
programs = [chr(a) for a in range(ord("a"), ord("p") + 1)]
mapping = {}
instructions = problem_data.split(",")
while rank < 1000000000:
    key = one_dance(programs, instructions)
    rank += 1
    if key not in mapping:
        mapping[key] = set()
    mapping[key].add(rank)
    print(rank, key)
print("".join(programs))
# l = [l[3], l[2], l[12], l[11], l[7], l[4], l[9], l[13], l[8], l[5], l[15], l[14], l[10], l[6], l[1], l[0]]
