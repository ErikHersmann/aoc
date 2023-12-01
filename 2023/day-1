with open("aoc/input.txt", "r", encoding="utf-8") as f:
    inp = f.readlines()
from util23 import table

res = 0
nums = "one, two, three, four, five, six, seven, eight, nine".split(", ")
dict = {"one":1, "two":2, "three":3, "four":4 ,"five":5, "six":6, "seven":7, "eight":8, "nine":9}

for idx,line in enumerate(inp):
    line = line.strip()
    cur = []

    for idx2,char in enumerate(line):
        try:
            cur.append(int(char))
        except:
            if line[idx2:idx2+3] in nums:
                cur.append(dict[line[idx2:idx2+3]])
            if line[idx2:idx2+4] in nums:
                cur.append(dict[line[idx2:idx2+4]])
            if line[idx2:idx2+5] in nums:
                cur.append(dict[line[idx2:idx2+5]])
    # print(cur)
    res += cur[0]*10 + cur[-1]
    
print(res)
