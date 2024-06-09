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
arr0 = sorted(arr0)
print(arr0[-1])
print(arr0[-1]+arr0[-2]+arr0[-3])
