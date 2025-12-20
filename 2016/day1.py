from email.mime import base
from enum import verify

from click import version_option
from helper import inp

# data = inp
num = 23

# Find closest uneven square that is smaller
# Find closest corner and calculate offset the result would be
# base uneven square + offset from horizontal or vertical (aka closest corner)

base_square = 1
while base_square**2 < num:
    base_square += 2
base_square -= 2
corner = 3
for corner_idx in range(4):
    center = base_square**2 + corner_idx*base_square + base_square//2 + 1 + 
    if base_square**2 + (corner_idx*base_square) > num:
        corner = corner_idx-1
        break
vertical = base_square
horizontal = (num -  (base_square**2 + (corner*base_square) + base_square//2))
print(horizontal + vertical)