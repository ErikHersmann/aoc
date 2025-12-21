from helper import problem_data
print(list(map(sum,zip(*[[len(line)-len(eval(line)), 2  + line.count("\\") + line.count('"')] for line in problem_data.splitlines()]))))
