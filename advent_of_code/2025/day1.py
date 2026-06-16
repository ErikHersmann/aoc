from helper import inp


# L is -
# R is +
# % 99


cur = 50
total = 0
res2 = 0
# inp ="""L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

    # The dial starts by pointing at 50.
    # The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    # The dial is rotated L30 to point at 52.
    # The dial is rotated R48 to point at 0.
    # The dial is rotated L5 to point at 95.
    # The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    # The dial is rotated L55 to point at 0.
    # The dial is rotated L1 to point at 99.
    # The dial is rotated L99 to point at 0.
    # The dial is rotated R14 to point at 14.
    # The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.


for line in inp.splitlines():
    sign = line[0]
    val = int(line[1:])
    if sign == "L":
        val *= -1
    # prev is between 0 and 99 => goes negative or wraps around
    # prev is between 0 and -99 => goes positive or wraps around
    prev = cur
    cur += val
    alr_increased = False
    # Positive previous
    if (prev > 0 and prev < 99):
        # Sign change
        if cur <= 0:
            res2 += 1 + cur // 100
            alr_increased = True
        # Out of bounds
        elif cur > 99:
            res2 += 1 + cur // 100
            alr_increased = True
    # Negative previous
    elif (prev < 0 and prev > -99):
        if cur >= 0:
            res2 += 1 + cur // 100
            alr_increased = True
        elif cur < -99:
            res2 += 1 + cur // 100
            alr_increased = True
    cur %= 100
    if cur == 0:
        total += 1
        if not alr_increased:
            res2 += 1
print(total)
print(res2)