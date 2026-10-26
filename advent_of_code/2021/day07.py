from statistics import mean, median
from helper import problem_data, maxsize

data = list(map(int, problem_data.split(",")))
# data = [16,1,2,0,4,2,7,1,2,14]
s, e = min(data), max(data)
best = maxsize
for m in range(s, e+1):
    total = 0
    for x in data:
        total += sum(range(1, 1+abs(m-x)))
    best = min(total, best)
print(best)

# Horribly inefficient but we get away with it
# We should start checking symmetrically from the middle since we only get worse towards the sides