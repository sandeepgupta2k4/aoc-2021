import sys
with open("input.txt") as fp:
    first = True
    boards = []
    board = []
    for line in fp:
        row = line.strip("\n")
        if first:
            nums = list(map(int, row.split(",")))
            first = False
            continue

        if not row.strip(" "):
            boards.append(board)
            board = []
            continue

        values = []
        l = row.strip(" ").split(" ")
        for val in l:
            if val and val != '':
                values.append([int(val), False])
        board.append(values)


def all_true(row):
    for val in row:
        if not val[1]:
            return False
    return True


def won(board):
    for row in board:
        if all_true(row):
            return True

    for j in range(len(board[0])):
        col = []
        for i in range(len(board)):
            col.append(board[i][j])
        if all_true(col):
            return True
    return False


def mark(board, num):
    for row in board:
        for val in row:
            if val[0] == num:
                val[1] = True


def score(board, num):
    total = 0
    for row in board:
        for val in row:
            if not val[1]:
                total += val[0]
    return total * num


boards.pop(0)
for num in nums:
    for board in boards:
        mark(board, num)
        if won(board):
            print(score(board, num))
            sys.exit(0)
