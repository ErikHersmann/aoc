from helper import input_data


def slow(cur, delta):
    temp = 0
    off = (1 if delta > 0 else -1)
    for _ in range(abs(delta)):
        cur += off
        temp += cur % 100 == 0
    return temp

data = input_data
pos = 50
res1 = 0
res2 = 0

for line in data.splitlines():
    val = int(line[1:]) * (-1 if line[0] == "L" else 1)
    res2 += slow(pos, val)
    pos += val
    res1 += pos % 100 == 0
print(res1)
print(res2)
