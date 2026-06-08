from helper import problem_data

t = problem_data
t += problem_data[0]
ptr = 1
total = 0
while ptr < len(t):
    prev, cur = map(int, t[ptr-1:ptr+1])
    total += prev if prev == cur else 0
    ptr += 1
print(total)

total = 0
for ptr in range(0, len(problem_data)):
    prev = int(problem_data[ptr])
    n = int(problem_data[(ptr+(len(problem_data)//2))%len(problem_data)])
    total += prev if prev == n else 0
    ptr += 1
print(total)
