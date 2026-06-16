from helper import problem_data


def main(part_1: bool):
    visited = set()
    santa, robot = (0, 0), (0, 0)
    for idx, instruction in enumerate(problem_data):
        visited.add(santa)
        visited.add(robot)
        x, y = 0, 0
        match instruction:
            case "^":
                y = 1
            case ">":
                x = 1
            case "<":
                x = -1
            case "v":
                y = -1
        if not part_1 and idx%2:
            robot = (robot[0]+y, robot[1] + x)
        else:
            santa = (santa[0] + y, santa[1] + x)
    return len(visited)

print(f"Part 1: {main(True)}")
print(f"Part 2: {main(False)}")