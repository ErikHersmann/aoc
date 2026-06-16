from math import prod
from helper import problem_data

# Greedy as long as all values > 0
# Greedy via sum of props for any ingredient (that's the best)
# or Z3


data = problem_data
ingredients = []
for line in data.splitlines():
    ingredients.append([int(x) for x in line.replace(",", "").split() if x.lstrip("-").isnumeric()])

# total = sum (ingredients[0][col])
# for col in range(1, 4)
# total *= sum (ingredients[row][col] for row in range(4))
