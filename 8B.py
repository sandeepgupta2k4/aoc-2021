with open("input.txt") as fp:
    lines = []
    data = []
    for line in fp:
        row = line.strip("\n")
        input = row.split("|")
        patterns = input[0].split(" ")
        output = input[1].split(" ")

        output.pop(0)
        data.append((patterns, output))


def detrmine_069(pattern, one, four):
    for char in one:
        if char not in pattern:
            return 6

    for c in four:
        if c not in pattern:
            return 0
    return 9


def detrmine_235(pattern, one, four):
    for char in one:
        if char not in pattern:
            mis_count = 0
            for c in four:
                if c not in pattern:
                    mis_count += 1
            if mis_count == 1:
                return 5
            else:
                return 2
    return 3


total = 0
for patterns, output in data:
    four = None
    one = None
    patterns.pop()
    digit_map = dict()
    for pattern in patterns:
        sorted_pattern = "".join(sorted(pattern))
        if len(pattern) == 2:
            digit_map[sorted_pattern] = 1
            digit_map[pattern] = 1
            one = pattern
        elif len(pattern) == 4:
            digit_map[sorted_pattern] = 4
            digit_map[pattern] = 4
            four = pattern
        elif len(pattern) == 3:
            digit_map[sorted_pattern] = 7
            digit_map[pattern] = 7
        elif len(pattern) == 7:
            digit_map[sorted_pattern] = 8
            digit_map[pattern] = 8

    for pattern in patterns:
        sorted_pattern = "".join(sorted(pattern))
        if len(pattern) == 6:
            d = detrmine_069(pattern, one, four)
            digit_map[pattern] = d
            digit_map[sorted_pattern] = d
        elif len(pattern) == 5:
            d = detrmine_235(pattern, one, four)
            digit_map[pattern] = d
            digit_map[sorted_pattern] = d

    digits = []
    for p in output:
        sp = "".join(sorted(p))
        if p in digit_map:
            digits.append(str(digit_map[p]))
        else:
            digits.append(str(digit_map[sp]))

    value = int("".join(digits))
    total += value

print(total)
