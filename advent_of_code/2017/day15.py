
from collections import deque
from time import time_ns


A = 783
B = 325
# A, B = 65, 8921
MOD = 2147483647
mask = 2**16 - 1


qA = deque()
qB = deque()
rank = 0
total = 0
pair = 0
while pair < 5*(10**6):
    A = (A*16807)%MOD
    B = (B*48271)%MOD
    if not A & 3:
        qA.append(A&mask)
        while min(len(qA), len(qB)) > 0:
            pair += 1
            if qA.popleft() == qB.popleft():
                total += 1
    if not B & 7:
        qB.append(B&mask)
        while min(len(qA), len(qB)) > 0:
            pair += 1
            if qA.popleft() == qB.popleft():
                total += 1
    rank += 1

print(total, rank)