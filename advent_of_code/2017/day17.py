

# positions = [0]
# pos = 0
# MOD = 354
# # MOD = 3
# while len(positions) <= 2017:
#     pos += MOD
#     pos %= len(positions)
#     pos += 1
#     positions.insert(pos, len(positions))
# print(positions[pos-2:pos+2])

# Just keep track of the position and length of the list
# Don't actually update the list we are only interested in the index whenever we insert at the index after 0
# whenever u insert at before the zero index (start at 0 and increment) we have to update the index after 0 and can keep the old value

length = 0
MOD = 354
# MOD = 3
pos = 0
limit = 50000000
zero_pos = 0
val_after_zero = None
while pos <=limit:
    length += 1
    pos += MOD
    pos %= length
    pos += 1
    if pos <= zero_pos:
        zero_pos += 1
    elif pos-1 == zero_pos:
        val_after_zero = length

print(val_after_zero)
# 1 2 555 99