from collections import defaultdict
from helper import problem_data, throw

PART_1 = False
data = problem_data
data = [line.split(" -> ") for line in data.splitlines()]
data[89] = ["956", "b"] if not PART_1 else data[89]
wires = defaultdict(int)

while len(data) > 0:
    line = data.pop(0)
    source, target = line
    source = source.split()
    match len(source):
        case 1:
            left = source[0]
            if left.isnumeric():
                wires[target] = int(left)
            else:
                if left in wires:
                    wires[target] = wires[left]
                else:
                    data.append(line)
        case 2:
            if source[1].isnumeric():
                wires[target] = ~int(source[1])
            else:
                if source[1] in wires:
                    wires[target] = ~ wires[source[1]]
                else:
                    data.append(line)
        case 3:
            left, op, right = source
            left = (
                int(left)
                if left.isnumeric()
                else wires[left] if left in wires else None
            )
            right = (
                int(right)
                if right.isnumeric()
                else wires[right] if right in wires else None
            )
            if left != None and right != None:
                match op:
                    case "AND":
                        wires[target] = left & right
                    case "OR":
                        wires[target] = left | right
                    case "LSHIFT":
                        wires[target] = left << right
                    case "RSHIFT":
                        wires[target] = left >> right
                    case _:
                        throw()
            else:
                data.append(line)
        case _:
            throw()

print(wires['a'])
