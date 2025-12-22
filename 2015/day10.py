from helper import problem_data, throw

data = problem_data
def compress(string: str):
    idx = 0
    temp = ""
    while idx < len(string):
        run = 1
        while idx < len(string)-1 and string[idx] == string[idx+1]:
            idx += 1
            run += 1
        temp += str(run)
        temp += string[idx]
        idx += 1
    return temp

for i in range(50):
    data = compress(data)
    if i == 40:
        print(f"Part 1: {len(data)}")
else:
    print(f"Part 2: {len(data)}")
