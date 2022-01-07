with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        lines.append(row)


def neighbor(grid, i, j):
    neighbors = []
    if i > 0:
        neighbors.append(grid[i-1][j])

    if i < len(grid) - 1:
        neighbors.append(grid[i+1][j])

    if j > 0:
        neighbors.append(grid[i][j-1])

    if j < len(grid[0]) - 1:
        neighbors.append(grid[i][j+1])

    return neighbors


def is_low(val, n):
    for nb in n:
        # print("{} {}".format(int(nb), val))
        if int(val) >= int(nb):
            # print("returning false")
            return False
    # print("returning true")
    return True


risk = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        neighbors = neighbor(lines, i, j)
        if is_low(lines[i][j], neighbors):
            # print("is low {} {} {}".format(i, j, lines[i][j]))
            # print(neighbors)
            risk += (int(lines[i][j]) + 1)
print(risk)
