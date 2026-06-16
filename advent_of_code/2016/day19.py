from helper import throw
from collections import deque


# this has a closed formula I'm sure of it 
# This is the jerusalems seat problem or smth

# 1 1
# 2 1
# 3 3
# 4 1
# 5 


# Remove all evens
# if the number of contestants was even first chair starts next round else the second chair 
# remove every second contestant
# Repeat with different starting element based on 

# 8 => 
#  1x2
# 3x4
# 5x6
# 7x8

# 1x3
# 5x 7
# 1x5

# Halve elements
# If even first element starts
# If uneven second element starts

# Gaps between first few elements are a function of round number ?

# target = 3005290
# target = 64
# _round = 1
# starter = 1
# while target > 1:
#     if target % 2:
#         starter += 2*_round
#     _round += 1
#     target //= 2
# print(starter)
# # 302 too low

problem_data = 3005290

l = deque(range(1, problem_data+1))
while len(l) > 1:
    # l.remove(l[len(l)//2])
    l.append(l.popleft())
    l.pop()
    # Pop opposite number instead ??
print(f"Part 1: {l.popleft()}")


# Why am I so braindead
# This should be a calculation instead of a simulation I believe
# And how do I get the opposite side seat
# Can I just do len(l)//2 as index ?



# 1 2 3 4 5 remaining

# pop 3 (5//2 = 2 correct index)
