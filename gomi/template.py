with open("aoc/input.txt", "r", encoding="utf-8") as f:
    inp = f.readlines()


res = 0


for idx,line in enumerate(inp):
    line = line.strip()
    if line == "":
        pass
    for word in line.split():
        print(word)

    print(idx, line)
    
print(res)