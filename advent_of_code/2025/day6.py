from helper import input_data

def cleanup_data_part_2(data: str):
    split_data = [x for x in data.splitlines()]
    split_data[4] += " " * (len(split_data[0]) - len(split_data[4]))
    ret_val = [[""] for _ in range(5)]
    for col_idx in range(len(split_data[0])):
        characters = [split_data[row_idx][col_idx] for row_idx in range(5)]
        if all([char == " " for char in characters]):
            for row_idx in range(5):
                ret_val[row_idx].append("")
        else:
            for row_idx in range(5):
                ret_val[row_idx][-1] += split_data[row_idx][col_idx]
    return ret_val

def solve_part_2(data: list):
    res = 0
    for element in range(len(data[0])):
        op = data[4][element]
        vals = [data[idx][element] for idx in range(4)]
        temps = []
        for idx2 in range(max([len(x) for x in vals])-1, -1, -1):
            temp = "".join([val if val != " " else "" for val in [y[idx2] for y in vals]])
            temps.append(temp)
        res += eval(op.join(temps))
    return res

data = input_data
res1 = 0
data = [x.split() for x in data.splitlines()]
for idx in range(len(data[0])):
    op = data[4][idx]
    numerators = [data[idx2][idx] for idx2 in range(4)]
    eq = op.join(numerators)
    val = eval(eq)
    res1 += val
print(f"Part 1: {res1}")


data2 = cleanup_data_part_2(input_data)
res2 = solve_part_2(data2)
print(f"Part 2: {res2}")

assert res1 == 6417439773370
assert res2 == 11044319475191
