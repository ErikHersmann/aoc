#i not in[8,13,16,17]

result = []
expected = [True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, False, False, True, True, True, True, True, True, True]
for x in range(25):
    result.append(x not in [8,13,16,17])

print(result == expected)