from helper import problem_data

strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def parse_line(line: str):
    output = []
    for idx, char in enumerate(line):
        if char.isnumeric():
            output.append(int(char))
        else:
            for s in strings:
                try:
                    if line[idx:idx+len(s)] == s:
                        output.append(strings.index(s)+1)
                        break
                except:
                    continue
    return int(f"{output[0]}{output[-1]}")

total = 0
total2 = 0
for line in problem_data.splitlines():
    total2 += parse_line(line)
    line = [x for x in line if x.isnumeric()]
    total += int("".join([line[0], line[-1]]))
print(total)
print(total2)
