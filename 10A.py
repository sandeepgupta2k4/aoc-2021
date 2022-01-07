with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        lines.append(row)


def process(line):
    stack = []
    char_map = dict()
    char_map[")"] = 3
    char_map["]"] = 57
    char_map["}"] = 1197
    char_map[">"] = 25137

    pair_map = dict()
    pair_map[")"] = "("
    pair_map["}"] = "{"
    pair_map["]"] = "["
    pair_map[">"] = "<"

    for char in line:
        if char in ["[", "(", "{", "<"]:
            stack.append(char)
        elif char in ["}", ")", "]", ">"]:
            val = stack.pop()
            if val != pair_map[char]:
                return False, char_map[char]

    return True, 0


score = 0
for line in lines:
    valid, val = process(line)
    if not valid and val > 0:
        score += val

print(score)
