with open("inputreal", "r") as f:
    data = f.readlines()

height = len(data)
width  = len(data[0])
numbers = [str(nr) for nr in range(0, 10)]
numbers2 = numbers[::]
numbers2.append(".")

def check_cell(x, y):
    global data, width, height
    output = []
    if x > 0:
        # L
        if data[x-1][y] == "*":
            output.append((x-1, y))
        if y > 0:
            # TL
            if data[x-1][y-1] == "*":
                output.append((x-1, y-1))
    if y > 0:
        # T
        if data[x][y-1] == "*":
            output.append((x, y-1))
        if x < width-2:
            # TR
            if data[x+1][y-1] == "*":
                output.append((x+1, y-1))
    if x < width-2:
        # R
        if data[x+1][y] == "*":
            output.append((x+1, y))
        if y < height - 2:
            # BR
            if data[x+1][y+1] == "*":
                output.append((x+1, y+1))
    if y < height - 2:
        # B
        if data[x][y+1] == "*":
            output.append((x, y+1))
        if x > 0:
            # BL
            if data[x-1][y+1] == "*":
                output.append((x-1, y+1))
    # print(x,y, output)
    if len(output) > 0:
        return (True, output)
    return (False, None)

total = []
gearindex = [[] for _ in range(10000)]
partindex = 0


for rowidx, line in enumerate(data):
    temp = ""
    passed = False
    num1 = 0
    num2 = 0
    for colidx, character in enumerate(line.strip()):
        if character in numbers:
            temp += character
            checked = check_cell(rowidx, colidx)
            if checked[0]:
                # print(checked)
                passed = True
                if checked[1]:
                    # print(checked)
                    for gear in checked[1]:
                        gearindex[partindex].append(gear)
            
        else:
            # We encounter a non number
            # Check if current temp has passed all checks
            if temp != "" and passed:
                total.append(int(temp))
                temp = ""
                gearindex[partindex]  = list(set(gearindex[partindex]))
                partindex += 1
            passed = False
            temp = ""
    # End of the line
    if temp != "" and passed:
        total.append(int(temp))
        temp = ""
        gearindex[partindex]  = list(set(gearindex[partindex]))
        partindex += 1


    """
    if rowidx < 1000:
        print(f"\nrow {rowidx+1} total {total} {[gear for gear in gearindex if gear]}")
"""
new_gear = []
for gears in gearindex:
    for gear in gears:
        new_gear.append(gear)
print(new_gear)
print(total)
tsum = 0


for idx1, (gears1, part1) in enumerate(zip(gearindex, total)):
    for idx2, (gears2, part2) in enumerate(zip(gearindex, total)):
        if idx1 < idx2:
            for gear in gears1:
                if gear in gears2 and new_gear.count(gear) == 2:
                    print(part1, part2, part1*part2)
                    tsum += part1*part2

print(tsum)