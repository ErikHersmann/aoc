positions = [0]
pos = 0
skip_count = 354
while len(positions) <= 2017:
    pos += skip_count
    pos %= len(positions)
    pos += 1
    positions.insert(pos, len(positions))
print(f"Part 1: {positions[pos+1]}")

length = 0
pos = 0
limit = 50000000
zero_pos = 0
val_after_zero = None
while length <= limit:
    length += 1
    pos = ((pos + skip_count) % length) + 1
    if pos <= zero_pos:
        zero_pos += 1
    elif pos - 1 == zero_pos:
        val_after_zero = length

print(f"Part 2: {val_after_zero}")
