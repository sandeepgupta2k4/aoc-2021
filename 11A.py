with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        lines.append(row)

grid = []
for i in range(len(lines)):
    row = []
    for j in range(len(lines[0])):
        row.append(int(lines[i][j]))
    grid.append(row)


def neighbor(grid, i, j):
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))
        if j > 0:
            neighbors.append((i-1, j-1))

        if j < len(grid[0]) - 1:
            neighbors.append((i-1, j+1))

    if i < len(grid) - 1:
        neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i+1, j-1))

        if j < len(grid[0]) - 1:
            neighbors.append((i+1, j+1))

    if j > 0:
        neighbors.append((i, j-1))

    if j < len(grid[0]) - 1:
        neighbors.append((i, j+1))

    return neighbors


def dfs(grid, visited, node):
    if node in visited:
        return

    visited.add(node)
    nbs = neighbor(grid, node[0], node[1])
    for n in nbs:
        grid[n[0]][n[1]] += 1

    for n in nbs:
        if grid[n[0]][n[1]] > 9:
            dfs(grid, visited, n)


def process(grid, visited):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                dfs(grid, visited, (i, j))

    flashes = 0
    for n in visited:
        if grid[n[0]][n[1]] > 9:
            grid[n[0]][n[1]] = 0
            flashes += 1
    return flashes


total = 0

for i in range(100):
    res = process(grid, set())
    total += res

print(total)
