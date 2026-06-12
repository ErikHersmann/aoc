from helper import problem_data, throw

d = {"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}
def main(part_1: bool):
    for line in problem_data.splitlines():
        line = line.split()
        line.pop(0)
        index = int(line.pop(0).rstrip(":"))
        while len(line) > 0:
            key = line.pop(0).rstrip(":")
            val = int(line.pop(0).rstrip(","))
            if not part_1:
                if key in ["cats", "trees"]:
                    if d[key] >= val:
                        break
                elif key in ["pomeranians","goldfish"]:
                    if d[key] <= val:
                        break
                else:
                    if d[key] != val:
                        break
            else:
                if d[key] != val:
                    break
        else:
            return index

            print(index)
print(f"Part 1: {main(True)}")
print(f"Part 2: {main(False)}")