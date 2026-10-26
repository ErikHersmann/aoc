from helper import problem_data, throw

# problem_data = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# """

part_1 = True
x, depth, aim = 0, 0, 0
for line in problem_data.splitlines():
    cmd, val = line.split()
    val = int(val)
    match cmd:
        case "forward":
            x += val
            if not part_1:
                depth += val*aim
        case "up":
            if part_1:
                depth -= val
            else:
                aim -= val
        case "down":
            if part_1:
                depth += val
            else:
                aim += val
        case _:
            throw()
print(x, depth, x*depth)