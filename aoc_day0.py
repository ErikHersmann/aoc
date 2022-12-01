with open("day0_input.txt", "r") as file:
    str0 = file.read()
c = 0
arr0 = []
for i in str0.splitlines():
    try:
        c += int(i)
    except :
        arr0 += [c]
        c = 0   


print(sorted(arr0))
print(69921+70450+72718)
