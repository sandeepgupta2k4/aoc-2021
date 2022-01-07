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


def neighbor_cor(grid, i, j):
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))

    if i < len(grid) - 1:
        neighbors.append((i+1, j))

    if j > 0:
        neighbors.append((i, j-1))

    if j < len(grid[0]) - 1:
        neighbors.append((i, j+1))

    return neighbors


def is_low(val, n):
    for nb in n:
        if int(val) >= int(nb):
            return False
    return True


def is_in_basin(node, basin, grid):
    return int(grid[node[0]][node[1]]) != 9


def bfs(node, visited, basin, grid):
    if node in visited:
        return
    visited.add(node)
    for nb in neighbor_cor(grid, node[0], node[1]):
        if nb not in visited and is_in_basin(nb, basin, grid):
            basin.add(nb)
            bfs(nb, visited, basin, grid)


basins = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        neighbors = neighbor(lines, i, j)
        if is_low(lines[i][j], neighbors):
            basin = set()
            visited = set()
            basin.add((i, j))
            bfs((i, j), visited, basin, lines)
            basins.append(basin)

basins.sort(key=lambda x: len(x), reverse=True)
print(len(basins[0]) * len(basins[1]) * len(basins[2]))
