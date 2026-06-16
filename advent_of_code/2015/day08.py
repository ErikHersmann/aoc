from helper import problem_data
print("\n".join([f"Part {idx+1}: {sol}" for idx, sol in enumerate(list(map(sum,zip(*[[len(line)-len(eval(line)), 2  + line.count("\\") + line.count('"')] for  line in problem_data.splitlines()]))))]))
