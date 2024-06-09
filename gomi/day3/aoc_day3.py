with open("day3_input.txt", "r") as file:
    s = file.read().split("\n")

c, d = 0,0
for i in s:
    s1 = int(i.split(",")[0].split("-")[0])
    e1 = int(i.split(",")[0].split("-")[1])
    s2 = int(i.split(",")[1].split("-")[0])
    e2 = int(i.split(",")[1].split("-")[1])
    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        c += 1
        # print(c, s1, e1, s2, e2)
    if (s2 <= e1 and e2 >= e1) or (s1 <= e2 and e1 >= e2):
        print(s2, e1, s1, e2)
        d+= 1
print(c, d)