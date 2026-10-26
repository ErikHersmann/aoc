from helper import problem_data


# part 1
problem_data = problem_data.splitlines()
bits = [0 for _ in range(len(problem_data[0]))]
total = len(problem_data)
for line in problem_data:
    for idx, c in enumerate([x for x in line]):
        bits[idx] += 1 if c == "1" else 0
# print(bits, total)
gamma = "".join(["0" if b >= total//2 else "1" for b in bits])
epsilon = "".join(["1" if b >= total//2 else "0" for b in bits])
print(int(gamma, 2) * int(epsilon, 2))




# part 2
oxygen = 0
ignored = set()
for position in range(len(problem_data[0])):
    ones, zeroes = set(), set()
    for idx, num in enumerate(problem_data):
        if idx in ignored:
            continue
        if num[position] == "1":
            ones.add(idx)
        else:
            zeroes.add(idx)
    if len(ones) + len(zeroes) <= 2:
        oxygen = problem_data[ones.pop()] if len(ones) else problem_data[zeroes.pop()]
    if len(ones) >= len(zeroes):
        ignored = ignored.union(zeroes)
    else:
        ignored = ignored.union(ones)

oxygen = int(oxygen, 2)

co2 = 0
ignored = set()
for position in range(len(problem_data[0])):
    ones, zeroes = set(), set()
    for idx, num in enumerate(problem_data):
        if idx in ignored:
            continue
        if num[position] == "1":
            ones.add(idx)
        else:
            zeroes.add(idx)
    if len(ones) + len(zeroes) <= 2:
        co2 = problem_data[zeroes.pop()] if len(zeroes) else problem_data[ones.pop()]
    if len(zeroes) <= len(ones):
        ignored = ignored.union(ones)
    else:
        ignored = ignored.union(zeroes)

co2 = int(co2, 2)
print(oxygen * co2)