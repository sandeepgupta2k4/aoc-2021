with open("input.txt") as fp:
    output = []
    input_line = ""
    first = True
    for line in fp:
        row = line.strip("\n")
        if first:
            input_line = row
            first = False
        elif not row:
            continue
        else:
            output.append(row)

print(input_line)
print(output)


def update(output):
    new_output = []
    count = 120
    first_row = ["." for j in range(len(output) + count)]
    for i in range(60):
        new_output.append(first_row)
    pad = '.' * 60
    for row in output:
        new_output.append(pad + "".join(row) + pad)
    for i in range(60):
        new_output.append(first_row)
    return new_output


def process(grid, i, j):
    neighbors = []
    if i > 0:
        if j > 0:
            neighbors.append(grid[i-1][j-1])
        else:
            neighbors.append(".")

        neighbors.append(grid[i-1][j])

        if j < len(grid[0]) - 1:
            neighbors.append(grid[i-1][j+1])
        else:
            neighbors.append(".")
    else:
        neighbors.append(".")
        neighbors.append(".")
        neighbors.append(".")

    if j > 0:
        neighbors.append(grid[i][j-1])
    else:
        neighbors.append(".")

    neighbors.append(grid[i][j])

    if j < len(grid[0]) - 1:
        neighbors.append(grid[i][j+1])
    else:
        neighbors.append(".")

    if i < len(grid) - 1:
        if j > 0:
            neighbors.append(grid[i+1][j-1])
        else:
            neighbors.append(".")

        neighbors.append(grid[i+1][j])

        if j < len(grid[0]) - 1:
            neighbors.append(grid[i+1][j+1])
        else:
            neighbors.append(".")
    else:
        neighbors.append(".")
        neighbors.append(".")
        neighbors.append(".")

    num = ""
    for n in neighbors:
        if n == '#':
            num += '1'
        else:
            num += '0'
    # print("{} {} {} {}".format(i, j, num, int(num, 2)))
    return int(num, 2)


# def is_edge(output, i, j):


def enhance(output, input_line):
    new_output = []
    lit_count = 0
    for i in range(len(output)):
        row = []
        for j in range(len(output[0])):
            num = process(output, i, j)
            # if num == 0 and is_edge(i, j):
            val = input_line[num]
            if val == '#':
                lit_count += 1
            row.append(val)
        new_output.append(row)
    return new_output, lit_count


def p(array):
    for row in array:
        print(" ".join(row))


new_output = update(output)
for i in range(2):
    new_output, lit_count = enhance(new_output, input_line)
    p(new_output)
    if i % 2 != 0:
        new_output[0] = '.' * len(new_output[0])
        new_output[len(new_output) - 1][0] = '.'
        new_output[len(new_output) - 1][len(new_output[0]) - 1] = '.'

    # new_output = update(new_output)
    print(len(new_output[0]))
    print(lit_count)
    print(lit_count - (len(new_output[0]) + 2))
