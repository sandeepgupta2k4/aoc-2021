with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        lines.append(int(row))

result = 0
prev_window = 0
for i in range(len(lines)-2):
    current_window = lines[i] + lines[i+1] + lines[i+2]
    if current_window > prev_window:
        result += 1
    prev_window = current_window
print(result - 1)
