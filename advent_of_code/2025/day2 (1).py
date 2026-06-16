from helper import input_data


data = input_data
data = [[int(x) for x in b.split("-")] for b in data.split(",")]
res1 = 0
res2 = 0
for start, end in data:
    for x in range(start, end+1):
        a = str(x)
        n = len(a)
        if n%2 == 0 and a[:n//2] *2 == a:
            res1 += x
        for repeat_length in range(1, n//2 + 1):
            if n%repeat_length == 0 and a[:repeat_length] * (n//repeat_length) == a:
                res2 += x
                break
print(res1)
print(res2)
