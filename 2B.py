with open("input.txt") as fp:
    lines = []
    down = 0
    forward = 0
    aim = 0
    for line in fp:
        row = line.strip("\n")
        command, count = row.split(" ")
        count = int(count)
        if command == 'forward':
            forward += count
            down += (aim * count)
        elif command == 'down':
            aim += count
        else:
            aim -= count

print(down * forward)
