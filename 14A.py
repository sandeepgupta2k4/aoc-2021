from collections import defaultdict

with open("input.txt") as fp:
    rules = dict()
    initial = None
    first = True
    for line in fp:
        row = line.strip("\n")
        if not row:
            continue
        if first:
            initial = row
            first = False
            continue
        left, right = row.split("->")
        left = left.strip(" ")
        right = right.strip(" ")
        rules[left] = right

print(rules)
n = 10
for i in range(10):
    j = 0
    result = []
    while j < len(initial) - 1:
        result.append(initial[j])
        key = initial[j] + initial[j+1]
        if key in rules:
            result.append(rules[key])
        j += 1
    result.append(initial[-1])
    initial = "".join(result)
    print(i)

char_dict = defaultdict(int)

for char in initial:
    char_dict[char] += 1

l = []

for key in char_dict:
    l.append((char_dict[key], key))

l.sort(key=lambda x: x[0])

print(l[len(l) - 1][0] - l[0][0])
