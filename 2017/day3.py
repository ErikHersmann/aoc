problem_data = 325489
problem_data = 12
lb, ub = 0, 0

# TODO: find lb, ub by enumerating square 
# Determine side
# Determine offset from center of side
# Offset center + offset start (lb)

powers = [1]
i = 1
while powers[-1] < problem_data:
    powers.append((i+2)**2)
    i += 2

lb = int(powers[-2])
ub = int(powers[-1])

diff = ub - lb
side_length = int(diff/4)
# r, t, l ,u
side = lb
side_idx = 0
while problem_data > side:
    side += side_length
    side_idx += 1
side -= side_length
side_idx -= 1
side_center = side + int(side_length/2)
solution = abs(problem_data - side_center) + len(powers) - 1
# 551 is too low
print(solution) # 30 should be 31, 1 should be 2
pass

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

# Corners have 3 neighbors
# Everything else has 

series = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806]

# the input data is somewhere along a side and not a corner
# meaning we have to include number before and below
# maybe just simulate this since it's a recursive closed formula