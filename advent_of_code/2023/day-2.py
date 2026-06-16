with open("aoc/input.txt", "r", encoding="utf-8") as f:
    inp = f.readlines()


res = 0
cur = []
res2 = 0

for idx,line in enumerate(inp):
    line = line.strip()
    green, blue, red = [], [], []
    if line == "":
        pass
    for c,word in enumerate(line.split()):
        
        if word == "green" or word=="green," or word=="green;":
            green.append(int(line.split()[c-1]))
        if word == "blue" or word=="blue," or word=="blue;":
            blue.append(int(line.split()[c-1]))
        if word == "red" or word =="red," or word=="red;":
            red.append(int(line.split()[c-1]))

    if max(green) <= 13 and max(blue) <=14 and max(red)<= 12:
        print(green, red, blue)
        res += int(line.split("Game ")[1].split(":")[0])
    res2 += max(green)*max(blue)*max(red)
    #print(idx, line)
    
print(res)
print(res2)