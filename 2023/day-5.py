with open("inpt2", "r") as f:
    data = [line.strip() for line in  f.readlines() if line.strip() != ""]

df = []
seeds = [int(s) for s in (data[0][7:]).split()]
seeds2 = []
for idx in range(0, len(seeds), 2):
    seeds2.append((seeds[idx], seeds[idx-1] + seeds[idx+1]))


for line in data[1:]:
    if ":" == line[-1]:
        df.append([])
    else:
        df[-1].append(line.split())




# Instead of working with an instance cur
# Instead work with the range directly and only move the start
# or Split the range into multiple if needed
def part1():
    cur = 0
    res = []
    print(seeds)
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

def part2():
    cur = 0
    res = []
    print(seeds2)
    for seedrange in seeds2:
        cur = [seedrange]
        for mapidx, mapping in enumerate(df):
            for crange in cur:
                print(crange)
                for cmap in mapping:
                    destStart, sourceStart, length = [int(s) for s in cmap]
                    sourceEnd = sourceStart - 1 + length
                    destEnd = destStart - 1 + length
                    cStart = crange[0]
                    cEnd = crange[1]

                    if sourceEnd >= cStart >= sourceStart:
                        # Append the mapped partial range
                        # Move the start of the original range up to the new correct one
                        break
                    if sourceEnd >= cEnd >= sourceStart:
                        # Append the mapped partial range
                        # Move the end of the original range to sourceStart
                        break

part2()