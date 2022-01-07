with open("input.txt") as fp:
    grid = []
    folds = []
    max_x = 0
    max_y = 0
    for line in fp:
        row = line.strip("\n")
        if "," in row:
            x, y = map(int, row.split(","))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            grid.append((y, x))
        elif "fold" in row:
            val = row.split(" ")[2]
            axis, v = val.split("=")
            folds.append((axis, int(v)))


array = [["." for j in range(max_x + 1)] for i in range(max_y + 1)]


def count_dots(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == '#':
                count += 1

    return count


def pr(array):
    for row in array:
        print(" ".join(row))


for item in grid:
    array[item[0]][item[1]] = '#'


def fold_x(array, val):
    start = val - (len(array) - val) + 1
    index = 0
    for i in range(start, val):
        for j in range(len(array[0])):
            i_val = len(array) - 1 - index
            if array[i][j] != '#':
                array[i][j] = array[i_val][j]
        index += 1

    array = array[:val+1]


def fold_y(array, val):
    start = val - (len(array[0]) - val) + 1
    for i in range(len(array)):
        index = 0
        for j in range(start, val):
            if array[i][j] != '#':
                array[i][j] = array[i][len(array[0]) - 1 - index]
            index += 1

    for i in range(len(array)):
        array[i] = array[i][:val+1]


for fold in folds:
    if fold[0] == 'x':
        fold_y(array, fold[1])

    elif fold[0] == 'y':
        fold_x(array, fold[1])

    print(count_dots(array))
    break
# pr(array)
