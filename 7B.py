with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        crabs = list(map(int, row.split(",")))


def align(crabs, pos):
    min_pos = pos
    total = 0
    for crab in crabs:
        n = abs(crab - min_pos)
        val = (n * (n+1)) / 2
        total += val

    return total


min_pos = float('inf')
for pos in range(len(crabs)):
    val = align(crabs, pos)
    if val < min_pos:
        min_pos = val
print(min_pos)
