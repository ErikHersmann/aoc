from collections import deque
from helper import problem_data

part_1 = 0
part_2_b = []
for line in problem_data.splitlines():
    q = deque()
    for c in line:
        match c:
            case ")":
                if q.pop() != '(':
                    part_1 += 3
                    break
            case ']':
                if q.pop() != '[':
                    part_1 += 57
                    break
            case '}':
                if q.pop() != '{':
                    part_1 += 1197
                    break
            case '>':
                if q.pop() != "<":
                    part_1 += 25137
                    break
            case _:
                q.append(c)
    else:
        part_2 =  0
        while len(q):
            cur = q.pop()
            part_2 *= 5
            match cur:
                case "(":
                    part_2 += 1
                case "[":
                    part_2 += 2
                case "{":
                    part_2 += 3
                case "<":
                    part_2 += 4
        part_2_b.append(part_2)

print(f"Part 1: {part_1}")
print(f"Part 2: {sorted(part_2_b)[len(part_2_b)//2]}")