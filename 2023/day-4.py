with open("aoc/input.txt", "r", encoding="utf-8") as f:
    inp = f.readlines()


res = 0
cards = [1]*len(inp)
cards2 = [1]*len(inp)


for idx,line in enumerate(inp):
    line = line.strip()
    temp = 0


    winning = line.split(" | ")[0][8:].strip().split(" ")
    my_nums = line.split(" | ")[1].strip().split(" ")
    for num in my_nums:
        if num in winning and num != '':
            temp += 1
    
    # print(idx, winning, my_nums, temp)
    if temp > 0:
        for _ in range(cards[idx]):
            for i in range(1, temp+1):
                cards[idx+i] += 1
            cards[idx] -= 1
            # print(idx, cards)
    for idx3,new in enumerate(cards):
        if cards2[idx3] < new:
            cards2[idx3] = new
    
print(sum(cards2))