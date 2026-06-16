from helper import input_data


data = input_data

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

res1 = 0
for line in data.splitlines():
    first = sorted([(int(x), idx) for idx, x in enumerate(line[:-1])], reverse=True, key=lambda y: y[0])
    # Find maximum numbers leftmost index and then find maximum to the right of it
    leftmost_max = min([val[1] for val in first if val[0] == first[0][0]])
    right_side = sorted([int(y) for y in line[leftmost_max + 1 :]], reverse=True)
    res1 += 10 * int(line[leftmost_max]) + max(right_side)
    pass
print(res1)



# part 2 insights:

# Check the line up to n - 12 inclusive 
# Find the maximum value + index there
# Start search for second in the range ( first maximum index + 1 to n - 11 inclusive)

# For i in range(12):
    # prev_idx = 0
    # limit_idx = n - i
    # for x in range(prev_idx, limit_idx):
        # Find max and idx
    # res2 += 10 ** (12-i) * max
    # prev_idx = idx