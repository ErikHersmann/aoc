from helper import input_data


data = input_data

def solve_line(line, digit_count: int):
    numerical = [int(x) for x in line]
    n = len(line)
    return_value = 0
    prev_idx = -1
    for digit_position in range(digit_count):
        cur_best_idx = prev_idx+1
        for cur_idx in range(prev_idx+1, n-digit_count+1+digit_position):
            if numerical[cur_idx] > numerical[cur_best_idx]:
                cur_best_idx = cur_idx
        prev_idx = cur_best_idx
        return_value += (10 ** (digit_count - 1 - digit_position)) * numerical[cur_best_idx]
    return return_value

res1 = 0
res2 = 0
for line in data.splitlines():
    res1 += solve_line(line, 2)
    res2 += solve_line(line, 12)
print(res1)
print(res2)
