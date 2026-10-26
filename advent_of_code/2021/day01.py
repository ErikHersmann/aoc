from helper import problem_data

data = problem_data

# data = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263
# """

total = 0
prev = None
for line in data.splitlines():
    cur = int(line.strip())
    if prev and prev < cur:
        total += 1
    prev = cur
print(total)

total = 0
data = [int(line.strip()) for line in data.splitlines()]
sliding = data[:3][::-1]
for num in data[3:]:
    print(sum(sliding))
    prev = sum(sliding)
    sliding.insert(0, num)
    sliding.pop(-1)
    if sum(sliding) > prev:
        total += 1
print(total)