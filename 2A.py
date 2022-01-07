with open("input.txt") as fp:
    lines = []
    down = 0
    forward = 0
    for line in fp:
        row = line.strip("\n")
        command, count = row.split(" ")
        count = int(count)
        if command == 'forward':
            forward += count
        elif command == 'down':
            down += count
        else:
            down -= count

print(down * forward)
