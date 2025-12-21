from xmlrpc.client import MAXINT
from helper import input_data, test_data
import itertools
import sympy
from sympy.abc import x,y
from sympy import Matrix, solve_linear_system
flatten = itertools.chain.from_iterable

data = input_data

data = [a.splitlines() for a in data.split("\n\n")]
data = list(map(lambda tline: [tline[0].split("X+")[1].strip(), tline[1].split("X+")[1].strip(), tline[2].split("X=")[1].strip()],data))

clean = []
for line in data:
    clean.append([])
    for val in line:
        val = val.replace(", Y+", " ")
        val = val.replace(", Y=", " ")
        first, second = map(int, val.split())
        clean[-1].append((first, second))
data = clean

def find_minimum_1(problem):
    # Inefficient dynamic program
    a, b, prize = problem
    global_best = [MAXINT]
    visited = set()
    def dynamic(x, y, cost):
        key = (x, y, cost)
        if key in visited: return
        visited.add(key)
        def oob():
         return prize[0] < x or prize[1] < y
        def found():
            return prize[0] == x and prize[1] == y
        if oob(): 
            return
        if found(): 
            global_best[0] = min(global_best[0], cost)
            return
        dynamic(x + a[0], y + a[1], cost + 3)
        dynamic(x + b[0], y + b[1], cost + 1)
    dynamic(0, 0, 0)
    if global_best[0] == MAXINT:
        return 0
    return global_best[0] 

def find_minimum_2(problem, factor):
    # Treat this is a linear combination problem of vectors trying to find equal  vector
    # l1 * A + l2 * B = C
    # Find l1 and l2 as natural numbers, otherwise return 0
    a, b, prize = problem
    (a1, a2) = a
    (b1, b2) = b
    (t1, t2) = prize
    t1 += factor
    t2 += factor
    system = Matrix(((a1, b1, t1), (a2, b2, t2)))
    retval = solve_linear_system(system, x,y)
    if not retval[x].is_integer or not retval[y].is_integer:
        return 0
    return retval[x] * 3 + retval[y]

total1 = 0
total2 = 0
for problem in data:
    total1 += find_minimum_2(problem, 0)
    total2 += find_minimum_2(problem, 10000000000000)
print(total1)
print(total2)