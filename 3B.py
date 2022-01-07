with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        lines.append(row)

result = []
eps = []
for i in range(len(lines[0])):
    zeros = 0
    ones = 0
    for j in range(len(lines)):
        if lines[j][i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        result.append("1")
        eps.append("0")
    else:
        result.append("0")
        eps.append("1")


gamma = int("".join(result), 2)
epsl = int("".join(eps), 2)

print(gamma)
print(epsl)
