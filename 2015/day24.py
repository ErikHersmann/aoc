from helper import problem_data
from math import prod
from itertools import permutations
from sys import maxsize

PART = 1
weights = [int(x.strip()) for x in problem_data.splitlines()][::-1]
total = sum(weights)
third = total // (3 if PART == 1 else 4)
# Left group is 5 numbers
best = [maxsize, None]
if PART == 1:
    n = len(weights)
    for i1 in range(n):
        for i2 in range(i1+1, n):
            for i3 in range(i2+1, n):
                for i4 in range(i3+1, n):
                    for i5 in range(i4+1, n):
                        for i6 in range(i5+1, n):
                            group = [
                                weights[i1]
                                ,weights[i2]
                                ,weights[i3]
                                ,weights[i4]
                                ,weights[i5]
                                ,weights[i6]
                            ]
                            s = sum(group)
                            if s > third:
                                continue
                            elif s < third:
                                break
                            product = prod(group)
                            if product < best[0]:
                                best = [product, [group]]
                            elif product == best[0]:
                                best[1].append(group)
elif PART == 2:
    for group in permutations(weights, 4):
        if sum(group) == third:
            product = prod(group)
            if product < best[0]:
                best = [product, [group]]
            elif product == best[0]:
                best[1].append(group)


print(best)
