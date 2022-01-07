from collections import defaultdict


class Graph:
    def __init__(self):
        self._adj = defaultdict(list)
        self.V = set()

    def vertices(self):
        return self.V

    def add(self, u, v):
        self._adj[u].append(v)
        self._adj[v].append(u)
        self.V.add(u)
        self.V.add(v)

    def adj(self, u):
        return self._adj[u]


def make_graph(edges):
    g = Graph()
    for edge in edges:
        g.add(edge[0], edge[1])
    return g


with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        u, v = row.split("-")
        lines.append((u, v))


def is_ok(path):
    small_visit_count = defaultdict(int)
    for nb in path:
        if nb.islower() and nb not in ["start", "end"]:
            small_visit_count[nb] += 1
    for v in small_visit_count:
        if small_visit_count[v] > 1:
            return False
    return True


def should_visit(nb, visited, path):
    if nb not in visited or nb.isupper():
        return True

    return nb.islower() and nb not in ["start", "end"] and is_ok(path)


def dfs(graph, node, visited, path, paths):
    visited.add(node)
    path.append(node)
    if node == "end":
        paths.append(list(path))
    else:
        for nb in graph.adj(node):
            if should_visit(nb, visited, path):
                dfs(graph, nb, visited, path, paths)
    path.pop()
    if node != "start" and node in visited and path.count(node) == 0:
        visited.remove(node)


graph = make_graph(lines)
paths = []
visited = set()

dfs(graph, "start", visited, [], paths)

print(len(paths))
