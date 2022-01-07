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
