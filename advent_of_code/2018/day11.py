
from collections import defaultdict
problem_data = 1723

def calc_power_level(x, y):
    rack_id = x + 10
    power_level =  rack_id * y
    power_level += problem_data
    power_level *= rack_id
    digit = int(str(power_level).zfill(3)[-3])
    digit -= 5
    return digit
three_by_threes = defaultdict(int)
best = 0
cord = None

for x in range(1, 301):
    for y in range(1, 301):
        pow_lvl = calc_power_level(x, y)
        for x_offset in range(3):
            for y_offset in range(3):
                key = (x-x_offset, y-y_offset)
                if min(key) > 0:
                    three_by_threes[key] += pow_lvl
                    if three_by_threes[key] > best:
                        best = three_by_threes[key]
                        cord = key
                    
print(best, cord)

# prefix sum of sorts or dp

# Start from the bottom right
# only consider 