from collections import defaultdict

with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        fishes = list(map(int, row.split(",")))

fish_map = defaultdict(int)
for fish in fishes:
    fish_map[fish] += 1


def simulate(count, days):
    fishes = []
    fishes.append(count)

    for i in range(days):
        additional_fish = 0
        for j in range(len(fishes)):
            if fishes[j] == 0:
                fishes[j] = 6
                additional_fish += 1
            else:
                fishes[j] -= 1

        for _ in range(additional_fish):
            fishes.append(8)
        # print("day {}".format(i))
    return fishes


def count(count, days):
    return len(simulate(count, days))


total = 0
# print(fish_map)


def create_map(fishes, fish_map, factor):
    for fish in fishes:
        fish_map[fish] += factor

    return fish_map


new_map = defaultdict(int)
for key in fish_map:
    create_map(simulate(key, 170), new_map, fish_map[key])

# print(new_map)
for key in new_map:
    total += (count(key, 86) * new_map[key])

print(total)
