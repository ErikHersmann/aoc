from helper import problem_data

def check_board_won(board) -> bool:
    # Rows
    for row in board:
        if all([x[1] for x in row]):
            return True
    # Cols
    for col in range(len(board[0])):
        temp_col = []
        for row in board:
            temp_col.append(row[col])
        if all([x[1] for x in temp_col]):
            return True
    # TL - BR
    # diag1 = [board[i][i] for i in range(len(board))]
    # if all([x[1] for x in diag1]):
    #     return True
    # # TR - BL
    # diag2 = [board[i][len(board)-i-1] for i in range(len(board))]
    # if all([x[1] for x in diag2]):
    #     return True
    return False

def calculate_winning_score(board, winning_number) -> bool:
    s = 0
    for line in board:
        for num, marked in line:
            if not marked:
                s += num
    return s * winning_number

data = problem_data.split("\n\n")
numbers = list(map(int, data[0].removeprefix("[").removesuffix("]").split(",")))

boards = []
for board in data[1:]:
    temp = []
    for line in board.splitlines():
        temp.append([[num, False] for num in list(map(int, line.split()))])
    boards.append(temp)


first = True
remaining = set(range(len(boards)))
for num in numbers:
    for b_idx, board in enumerate(boards):
        if b_idx not in remaining:
            continue
        for r_idx in range(len(board)):
            for c_idx in range(len(board[0])):
                if board[r_idx][c_idx][0] == num:
                    board[r_idx][c_idx] = [num, True]
                    if check_board_won(board):
                        if first:
                            print(calculate_winning_score(board, num))
                            first = False
                        if len(remaining) == 1:
                            print(calculate_winning_score(board, num))
                        remaining.remove(b_idx)
                    break