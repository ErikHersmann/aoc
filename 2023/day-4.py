with open("4inp", "r", encoding="utf-8") as f:
    inp = f.readlines()


points = [0 for _ in range(len(inp))]

for idx, line in enumerate(inp):
    line = line.strip()
    winning = line.split(" | ")[0][8:].strip().split()
    my_nums = line.split(" | ")[1].strip().split()
    for num in my_nums:
        if num in winning:
            if points[idx] == 0:
                points[idx] = 1
            else:
                points[idx] *= 2
    
    # print(idx, winning, my_nums, points)

print(sum(points))