from helper import problem_data


# d = {(-1, -1): 7, (0, -1): 8, (1, -1): 9, (-1, 0): 4, (0,0): 5, (1, 0): 6, (-1, 1): 1, (0, 1): 2, (1, 1): 3}
# current = (0, 0)
# for line in problem_data.splitlines():
#     for char in line:
#         match char:
#             case "U":
#                 current = (current[0], min(current[1] +1, 1))
#             case "L":
#                 current = (max(current[0]-1, -1), current[1])
#             case "R":
#                 current = (min(current[0]+1, 1), current[1])
#             case "D":
#                 current = (current[0], max(current[1] - 1, -1))
#     print(current, d[current])

current = (-2, 0)
d = {
    (-2, 0): "5",
    (-1, 0): "6",
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (-1, -1): "A",
    (0, -1): "B",
    (1, -1): "C",
    (0, -2): "D",
    (-1, 1): "2",
    (0, 1): "3",
    (1, 1): "4",
    (0, 2): "1",
}

for line in problem_data.splitlines():
    for char in line:
        match char:
            case "U":
                inc = (0, 1)
            case "L":
                inc = (-1, 0)
            case "R":
                inc = (1, 0)
            case "D":
                inc = (0, -1)
        current = (current[0] + inc[0], current[1] + inc[1])
        if (abs(current[0]) + abs(current[1])) >= 3:
            current = (current[0] - inc[0], current[1] - inc[1])
    print(current, d[current])