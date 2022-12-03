with open("day2_input.txt", "r") as file:
    s = file.read().split("\n")
first, second = "", ""
elves = ""
c,d = 0,0
already = []
line = 2
for i in s:
    if (line+1)%3 == 0:
        for a in s[line-2]:
            if a in s[line-1] and a in s[line] and a not in already:
                already += [a]
                if a.isupper():
                    d += ord(a)-38
                else:
                    d += ord(a)-96
    line += 1
    already = []


for i in s:
    first = i[:int((len(i)/2))]
    second = i[int((len(i)/2)):]
    already = []
    for j in first:
        if j in second and j not in already:
            already += [j]
            if j.isupper():
                c += ord(j)-38
                # print(j, ord(j)-38)
            else:
                c += ord(j)-96
                # print(j, ord(j)-96)   

print(c, d)