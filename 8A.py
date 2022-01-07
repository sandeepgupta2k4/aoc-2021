with open("input.txt") as fp:
    lines = []
    outputs = []
    for line in fp:
        row = line.strip("\n")
        input = row.split("|")
        pattern = input[0].split(" ")
        output = input[1].split(" ")
        output.pop(0)
        outputs.append(output)

total = 0
for output in outputs:
    for pattern in output:
        if len(pattern) in [2, 3, 4, 7]:
            total += 1

print(total)
