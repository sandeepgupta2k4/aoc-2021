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

pair_map = defaultdict(int)

j = 0
while j < len(initial) - 1:
    pair_map[initial[j] + initial[j+1]] += 1
    j += 1

for i in range(40):
    temp_dict = defaultdict(int)
    for pair in pair_map:
        if pair in rules:
            count = pair_map[pair]
            pair_map[pair] = 0
            val = rules[pair]
            key1 = pair[0] + val
            key2 = val + pair[1]
            temp_dict[pair[0] + val] += count
            temp_dict[val + pair[1]] += count
        else:
            temp_dict[pair] = pair_map[pair]

    pair_map = temp_dict

char_dict = defaultdict(int)
for pair in pair_map:
    char_dict[pair[0]] += pair_map[pair]
char_dict[initial[-1]] += 1


l = sorted(char_dict.items(), key=lambda x: x[1])
print(l[len(l) - 1][1] - l[0][1])
