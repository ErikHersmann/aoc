from helper import input_data


def part_1(available: list, fresh: list):
    fresh_available = set()
    for ingredient in available:
        for start, end in fresh:
            if start <= ingredient <= end:
                fresh_available.add(ingredient)
                break
    print(len(fresh_available))
    return len(fresh_available)


data = input_data

# data = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""

fresh, available = [x.splitlines() for x in data.split("\n\n")]
available = [int(x) for x in available]
fresh = [[int(x[0]), int(x[1])] for x in [y.split("-") for y in fresh]]
part_1(available=available, fresh=fresh)
fresh = sorted(fresh, key=lambda x: x[1])

# merge ranges and then calculate end-start

print(sum([x[1]-x[0] for x in fresh]))
res2 = 0
while len(fresh) > 1:
    (current_start, current_end) = fresh.pop(0)
    (next_start, next_end) = fresh[0]
    # This fails, please investigate
    assert(current_start <= next_start)
    assert(current_end <= next_end)
    # Not all overlap cases are handled
    if current_end < next_start:
        # No overlap
        res2 += current_end-current_start + 1
    else:
        # This handles the case that
        # merge but also skip this next time
        next = fresh.pop(0)
        fresh.insert(0, [current_start, next[1]])
if len(fresh) == 1:
    (current_start, current_end) = fresh.pop(0)
    res2 += current_end-current_start+1
print(res2)
