from helper import problem_data

total = 0
part_2 = 0
for row in problem_data.splitlines():
    row = [int(x) for x in row.strip().split()]
    s_row = sorted(row)
    diff = s_row[-1] - s_row[0]
    total += diff
    found = False
    for i in range(len(row)):
        if found:
            break
        for j in range(len(row)):
            if i == j:
                continue
            if row[i] % row[j] == 0:
                part_2 += row[i]//row[j]
                found = True
                break
    pass
print(total)
print(part_2)