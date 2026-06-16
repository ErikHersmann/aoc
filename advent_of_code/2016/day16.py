problem_data = "10111100110001111"
length = 272
length = 35651584


def dragon(data):
    atad = data[::-1]
    ones = "1" * len(data)
    b = "".join(["1" if a != b else "0" for a,b in zip(atad, ones)])
    return data + "0" + b


def checksum(data):
    return "".join(["1" if data[i] == data[i + 1] else "0" for i in range(0, len(data), 2)])


while len(problem_data) < length:
    problem_data = dragon(problem_data)

problem_data = problem_data[:length]

while len(problem_data) % 2 == 0:
    problem_data = checksum(problem_data)

print(f"Part 2: {problem_data}")
