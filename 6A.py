from collections import defaultdict

with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        fishes = list(map(int, row.split(",")))

fish_map = defaultdict(int)
for fish in fishes:
    fish_map[fish] += 1


for i in range(256):
    additional_fish = 0
    for j in range(len(fishes)):
        if fishes[j] == 0:
            fishes[j] = 6
            additional_fish += 1
        else:
            fishes[j] -= 1

    for f in range(additional_fish):
        fishes.append(8)

    print(len(fishes))
