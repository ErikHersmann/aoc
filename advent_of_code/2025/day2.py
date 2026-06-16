from helper import input_data, short_test, long_test


data = input_data

# data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""


data = [[int(x) for x in b.split("-")] for b in data.split(",")]
res1 = 0
for start, end in data:
    for x in range(start, end+1):
        a = str(x)
        n = len(a)
        for repeat_length in range(1, n//2 + 1):
            if n%repeat_length != 0: continue
            if a[:repeat_length] * (n//repeat_length) == a:
                res1 += x
                # print(x)
                break
        # if len(a) % 2 != 0: continue
        # if a[: len(a) // 2] == a[len(a) // 2 :]:
        #     res1 += x
        # From 2 to len(a) // 2
    pass
print(res1)