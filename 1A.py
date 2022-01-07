with open("input.txt") as fp:
    lines = []
    prev = 0
    current = 0
    result = 0
    for line in fp:
        row = line.strip("\n")
        current = int(row)
        if current > prev:
            result += 1
        prev = current
print(result-1)
