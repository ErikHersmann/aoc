with open("day1_input.txt", "r") as file:
    s = file.read().split("\n")
a,c = 0, 0  
for i in s:
    if i.split(" ")[0] == "A" and i.split(" ")[1] == "X":
        a += 1+3
    elif i.split(" ")[0] == "A" and i.split(" ")[1] == "Y":
        a += 2+6
    elif i.split(" ")[0] == "A" and i.split(" ")[1] == "Z":
        a += 3
    elif i.split(" ")[0] == "B" and i.split(" ")[1] == "X":
        a += 1
    elif i.split(" ")[0] == "B" and i.split(" ")[1] == "Y":
        a += 2+3
    elif i.split(" ")[0] == "B" and i.split(" ")[1] == "Z":
        a += 3+6
    elif i.split(" ")[0] == "C" and i.split(" ")[1] == "X":
        a += 1+6
    elif i.split(" ")[0] == "C" and i.split(" ")[1] == "Y":
        a += 2
    elif i.split(" ")[0] == "C" and i.split(" ")[1] == "Z":
        a += 3+3
for i in s:
    if i.split(" ")[0] == "A" and i.split(" ")[1] == "X":
        c += 3
    elif i.split(" ")[0] == "A" and i.split(" ")[1] == "Y":
        c += 1+3
    elif i.split(" ")[0] == "A" and i.split(" ")[1] == "Z":
        c += 2+6
    elif i.split(" ")[0] == "B" and i.split(" ")[1] == "X":
        c += 1
    elif i.split(" ")[0] == "B" and i.split(" ")[1] == "Y":
        c += 2+3
    elif i.split(" ")[0] == "B" and i.split(" ")[1] == "Z":
        c += 3+6
    elif i.split(" ")[0] == "C" and i.split(" ")[1] == "X":
        c += 2
    elif i.split(" ")[0] == "C" and i.split(" ")[1] == "Y":
        c += 6
    elif i.split(" ")[0] == "C" and i.split(" ")[1] == "Z":
        c += 7
# pretty ugly code
print(a, c)
