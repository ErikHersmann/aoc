with open("day5_input.txt", "r") as file:
    s = file.read()
c = 3
for i in s:
    c += 1
    if len(set((s[c-3], s[c-2], s[c-1], s[c]))) == 4:
        print(c+1)
        break
for i in s:
    c += 1
    if len(set((s[c-13], s[c-12], s[c-11], s[c-10], s[c-9], s[c-8], s[c-7],s[c-6],s[c-5],s[c-4] ,s[c-3], s[c-2], s[c-1], s[c]))) == 14:
        print(c+1)
        break




    













# a = [3, 4 , 5]; print(a[-2:]) # last n elements; print(a[::-1]) # reverse array