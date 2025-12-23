from math import prod
from helper import problem_data

data = problem_data
PART_TWO = False

ingredients = []
for line in data.splitlines():
    ingredients.append(
        [int(x) for x in line.replace(",", "").split() if x.lstrip("-").isnumeric()]
    )
properties = [[ingredient[idx] for ingredient in ingredients] for idx in range(5)]
pass
props_short = properties[:4]

best = 0
# Whole approach is just brute force, is there some smarter way to do this ?
for x1 in range(0, 101):
    for x2 in range(0, 101):
        for x3 in range(0, 101):
            for x4 in range(0, 101):
                if (x1 + x2 + x3 + x4) != 100 or (PART_TWO and sum([a * b for a, b in zip([x1, x2, x3, x4], properties[4])]) != 500):
                    continue
                # Add early termination conditions here for speed ?
                sums = [
                    sum([a * b for a, b in zip([x1, x2, x3, x4], prop)])
                    for prop in props_short
                ]
                if any([x < 0 for x in sums]):
                    continue
                best = max(
                    best,
                    prod(
                        sums
                    ),
                )
print(best)