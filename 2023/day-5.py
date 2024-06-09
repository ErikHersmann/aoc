with open("inpt2", "r") as f:
    data = [line.strip() for line in  f.readlines() if line.strip() != ""]

df = []
seeds = [int(s) for s in (data[0][7:]).split()]


for line in data[1:]:
    if ":" == line[-1]:
        df.append([])
    else:
        df[-1].append(line.split())



cur = 0
res = []
print(seeds)
# Instead of working with an instance cur
# Instead work with the range directly and only move the start
# or Split the range into multiple if needed
for seed in seeds:
    cur = seed
    for mapidx, mapping in enumerate(df):
        mapped = False
        # print(f"map {mapidx}")
        for cmap in mapping:
            destStart, sourceStart, length = [int(s) for s in cmap]
            sourceEnd = sourceStart - 1 + length
            destEnd = destStart - 1 + length
            if sourceEnd >= cur >= sourceStart:
                # print(f"cur {cur} source ({sourceStart} - {sourceEnd}) destination ({destStart} - {destEnd})")
                cur = destStart + cur - sourceStart
                break
    res.append(cur)

print(res)
print(min(res))