with open("4inp", "r", encoding="utf-8") as f:
    inp = f.readlines()


redo = [1 for _ in range(len(inp))]

for idx, line in enumerate(inp):
    line = line.strip()
    winning = line.split(" | ")[0][8:].strip().split()
    my_nums = line.split(" | ")[1].strip().split()
    idx2 = idx + 1
    for num in my_nums:
        if num in winning:
            redo[idx2] += 1 * redo[idx]
            idx2+=1
    
    # print(idx, winning, my_nums, points)

print(sum(redo))