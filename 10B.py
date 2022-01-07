with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        lines.append(row)


def process(line):
    stack = []
    pair_map = dict()
    pair_map[")"] = "("
    pair_map["}"] = "{"
    pair_map["]"] = "["
    pair_map[">"] = "<"

    cha_map = dict()
    cha_map["("] = 1
    cha_map["["] = 2
    cha_map["{"] = 3
    cha_map["<"] = 4

    for char in line:
        if char in ["[", "(", "{", "<"]:
            stack.append(char)
        elif char in ["}", ")", "]", ">"]:
            val = stack.pop()
            if val != pair_map[char]:
                return False, 0

    score = 0
    if len(stack) > 0:
        for i in range(len(stack)-1, -1, -1):
            score *= 5
            score += cha_map[stack[i]]
        return False, score
    return True, 0


scores = []
for line in lines:
    valid, val = process(line)
    if not valid and val > 0:
        scores.append(val)

scores.sort()
print(scores[len(scores)/2])
