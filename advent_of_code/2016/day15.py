# Similar to day 13 from 2017 part 2
from helper import problem_data

def main(part_one: bool):
    inp = []
    for line in problem_data.splitlines():
        line = line.split()
        inp.append(tuple(map(int, [line[3].lstrip("#"), line[11].rstrip(".")])))
    if not part_one:
        inp.append((11, 0))

    delay = 1
    while any([(tup[1] + delay + idx)%tup[0] for idx, tup in enumerate(inp)]):
        delay += 1
    return delay - 1

print(f"Part 1: {main(True)}")
print(f"Part 2: {main(False)}")