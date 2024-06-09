with open("day2_input.txt", "r") as file:
    s = file.read().split("\n")
def score(x):
    if x.isupper():
        d += ord(a)-38
    else:
        d += ord(a)-96
first, second = "", ""
p1, p2 = 0,0
already = []
line = 2
for i in s:
    first = i[:int((len(i)/2))]
    second = i[int((len(i)/2)):]
    already = []
    for j in first:
        if j in second and j not in already:
            already += [j]
            p1 += score(j)
for i in s:
    if (line+1)%3 == 0:
        for a in s[line-2]:
            if a in s[line-1] and a in s[line] and a not in already:
                already += [a]
                p2 += score(a)
    line += 1
    already = []

print(p1, p2)
