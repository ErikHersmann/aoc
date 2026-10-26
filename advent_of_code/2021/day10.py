from collections import deque
from helper import problem_data

score = 0
part_2 =  0
for line in problem_data.splitlines():
    q = deque()
    for c in line:
        match c:
            case ")":
                if q.pop() != '(':
                    score += 3
                    break
            case ']':
                if q.pop() != '[':
                    score += 57
                    break
            case '}':
                if q.pop() != '{':
                    score += 1197
                    break
            case '>':
                if q.pop() != "<":
                    score += 25137
                    break
            case _:
                q.append(c)
    else:
        pass
        # Trivially iterate stack here if we didn't break

print(score)