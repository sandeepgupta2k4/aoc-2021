from queue import PriorityQueue

with open("input.txt") as fp:
    lines = []
    for line in fp:
        l = []
        row = line.strip("\n")

        for char in row:
            l.append(int(char))

        new_l = []
        temp = []
        factor = 0

        for i in range(5):
            for val in l:
                risk = val + factor
                if risk > 9:
                    risk = 1
                new_l.append(risk)
                temp.append(risk)
            l = temp
            temp = []
            factor = 1

        lines.append(new_l)


factor = 0
grid = []
new_l = []
new_lines = []
for i in range(5):
    for line in lines:
        for val in line:
            risk = val + factor
            if risk > 9:
                risk = 1
            new_l.append(risk)
        new_lines.append(new_l)
        new_l = []

    for line in new_lines:
        grid.append(line)

    lines = new_lines
    new_lines = []
    factor = 1


lines = grid


def neighbors(grid, i, j):
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


unvisited = set()
vals = dict()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        unvisited.add((i, j))
        vals[(i, j)] = float('inf')


def dijkstra(lines, vals, unvisited):
    q = PriorityQueue()
    q.put((0, (0, 0)))
    while q.not_empty and len(unvisited) > 0:
        _, node = q.get()
        nbs = neighbors(lines, node[0], node[1])
        for nb in nbs:
            if nb in unvisited:
                dist = vals[(node[0], node[1])] + lines[nb[0]][nb[1]]
                if dist < vals[(nb[0], nb[1])]:
                    vals[(nb[0], nb[1])] = dist
                    q.put((dist, nb))
        unvisited.remove(node)
        print(len(unvisited))


vals[(0, 0)] = 0
dijkstra(lines, vals, unvisited)
print(vals[(len(lines)-1, len(lines[0])-1)])
