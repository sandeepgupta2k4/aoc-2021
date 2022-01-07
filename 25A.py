import sys
with open("input.txt") as fp:
    lines = []
    first = True
    for line in fp:
        row = line.strip("\n")
        l = []
        for c in row:
            l.append(c)
        lines.append(l)


def run(lines):
    result = [['.' for j in range(len(lines[0]))] for i in range(len(lines))]
    move_set = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '>' and (i, j) not in move_set:
                if j < len(lines[0]) - 1:
                    if lines[i][j+1] == '.':
                        result[i][j] = '.'
                        result[i][j+1] = '>'
                        move_set.add((i, j+1))
                    else:
                        result[i][j] = '>'
                else:
                    if lines[i][0] == '.':
                        result[i][j] = '.'
                        result[i][0] = '>'
                        move_set.add((i, 0))
                    else:
                        result[i][j] = '>'

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'v' and (i, j) not in move_set:
                if i < len(lines) - 1:
                    if lines[i+1][j] != 'v' and result[i+1][j] == '.':
                        result[i][j] = '.'
                        result[i+1][j] = 'v'
                        move_set.add((i + 1, j))
                    else:
                        result[i][j] = 'v'
                else:
                    if lines[0][j] != 'v' and result[0][j] == '.':
                        result[i][j] = '.'
                        result[0][j] = 'v'
                        move_set.add((0, j))
                    else:
                        result[i][j] = 'v'

    return result, len(move_set) > 0


def pr(lines):
    for row in lines:
        print(" ".join(row))
    print("\n")


result = list(lines)
i = 0
while True:
    result, moved = run(result)
    i += 1
    if not moved:
        print(i)
        break
