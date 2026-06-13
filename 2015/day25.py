def get_next(coordinate):
    (row, col) = coordinate
    if row == 1:
        return (col + 1, 1)
    return (row - 1, col + 1)


def calculate(value):
    return (value * 252533) % 33554393


target = (2981, 3075)
coord = (1, 1)
prev = 20151125
while coord != target:
    coord = get_next(coord)
    prev = calculate(prev)
print(f"Part 1: {prev}")
