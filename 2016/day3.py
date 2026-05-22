from helper import problem_data

possible = 0
lists = [[], [], []]
for line in problem_data.splitlines():
    a = [int(x) for x in line.split()]
    for i in range(3):
        lists[i].append(a[i])
    # a = [int(x) for x in sorted(line.split())]
    # possible += 1 if all([(a[0] + a[1]) > a[2], (a[0] + a[2]) > a[1], (a[1] + a[2]) > a[0]]) else 0

for a in lists:
    for i in range(0, len(a), 3):
        possible += 1 if all([(a[i] + a[i+1]) > a[i+2], (a[i] + a[i+2]) > a[i+1], (a[i+1] + a[i+2]) > a[i]]) else 0
print(possible)
