from collections import defaultdict
from helper import problem_data
from itertools import permutations

data = problem_data

neighbors = defaultdict(dict)
people = set()
for line in data.splitlines():
    line = line.split()
    a, num, b = line[0], (-1 if line[2] == "lose" else 1)* int(line[3]), line[-1][:-1]
    neighbors[a][b] = num
    people.add(a)
for person in people:
    neighbors["subols"][person] = 0
    neighbors[person]["subols"] = 0

pairs = {}
for person in neighbors:
    for other_person in neighbors[person]:
        pairs[(person, other_person)] = (
            neighbors[person][other_person] + neighbors[other_person][person]
        )

best = 0
for seating in permutations(neighbors.keys(), len(neighbors)):
    best = max(
        best,
        sum(
            pairs[(seating[i], seating[(i + 1) % len(seating)])]
            for i in range(len(seating))
        ),
    )
print(best)