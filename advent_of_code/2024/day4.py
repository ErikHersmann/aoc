from helper import input_data, test_data


data = [[b for b in a] for a in input_data.splitlines()]
Nrow = len(data)
Ncol = len(data[0])
result1 = 0
result2 = 0


def check_1(row, col):
    def search(xdir, ydir):
        # Parse out illegal moves
        for offset, dir, max_dir in zip([ydir, xdir], [row, col], [Nrow, Ncol]):
            if offset == -1 and dir < 3:
                return 0
            if offset == 1 and dir > max_dir - 4:
                return 0
        # Check
        for i, letter in zip(range(1, 4), ["M", "A", "S"]):
            if data[row + i * ydir][col + i * xdir] != letter:
                return 0
        return 1

    total = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            total += search(x, y)
    return total


def check_2(row, col):
    correct = ["M", "S"]
    if row > 0 and col < Ncol - 1 and row < Nrow - 1 and col > 0:
        if sorted([data[row - 1][col - 1], data[row + 1][col + 1]]) != correct:
            return 0
        if sorted([data[row - 1][col + 1], data[row + 1][col - 1]]) != correct:
            return 0
        return 1
    return 0


for row in range(Nrow):
    for col in range(Ncol):
        if data[row][col] == "X":
            result1 += check_1(row, col)
        if data[row][col] == "A":
            result2 += check_2(row, col)
print(result1)
print(result2)
