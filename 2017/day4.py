from helper import problem_data

valids = 0
valids_2 = 0


for line in problem_data.splitlines():
    line = line.split()
    valids += len(set(line)) == len(line)
    line = ["".join(sorted([c for c in item])) for item in line]
    valids_2 += len(set(line)) == len(line)

print(valids)
print(valids_2)