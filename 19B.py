import sys
from collections import defaultdict

with open("input.txt") as fp:
    nums = []
    scanners = []
    scanner = []
    for line in fp:
        row = line.strip("\n")
        if not row:
            scanners.append(scanner)
            scanner = []
        elif "scanner" in row:
            continue
        else:
            x, y, z = map(int, row.split(","))
            scanner.append((x, y, z))

or_dict = dict()
or_dict[0] = [lambda x, y, z: (x, y, z)]


def orientations(i, scanner_found):
    if i in scanner_found:
        return [lambda x, y, z: (x, y, z)]

    if i in or_dict:
        return or_dict[i]

    ors = []
    # ors.append(lambda x, y, z: (x, y, z))
    ors.append(lambda x, y, z: (x, y, z))

    # ors.append(lambda x, y, z: (x, 0 - y, 0 - z))
    ors.append(lambda x, y, z: (x, 0 - y, 0 - z))

    # ors.append(lambda x, y, z: (x, 0 - z, y))
    ors.append(lambda x, y, z: (x, z, 0 - y))

    # ors.append(lambda x, y, z: (x, z, 0 - y))
    ors.append(lambda x, y, z: (x, 0 - z, y))

    # ors.append(lambda x, y, z: (0 - x, 0 - y, z))
    ors.append(lambda x, y, z: (0 - x, 0 - y, z))

    # ors.append(lambda x, y, z: (0 - x, y, 0 - z))
    ors.append(lambda x, y, z: (0 - x, y, 0 - z))

    # ors.append(lambda x, y, z: (0 - x, 0 - z, 0 - y))
    ors.append(lambda x, y, z: (0 - x, 0 - z, 0 - y))

    # ors.append(lambda x, y, z: (0 - x, z, y))
    ors.append(lambda x, y, z: (0 - x, z, y))

    # ors.append(lambda x, y, z: (y, z, x))
    ors.append(lambda x, y, z: (z, x, y))

    # ors.append(lambda x, y, z: (y, 0 - x, z))
    ors.append(lambda x, y, z: (0 - y, x, z))

    # ors.append(lambda x, y, z: (y, x, 0 - z))
    ors.append(lambda x, y, z: (y, x, 0 - z))

    # ors.append(lambda x, y, z: (y, 0 - z, 0 - x))
    ors.append(lambda x, y, z: (0 - z, x, 0 - y))

    # ors.append(lambda x, y, z: (0 - y, x, z))
    ors.append(lambda x, y, z: (y, 0 - x, z))

    # ors.append(lambda x, y, z: (0 - y, 0 - x, 0 - z))
    ors.append(lambda x, y, z: (0 - y, 0 - x, 0 - z))

    # ors.append(lambda x, y, z: (0 - y, 0 - z, x))
    ors.append(lambda x, y, z: (z, 0 - x, 0 - y))

    # ors.append(lambda x, y, z: (0 - y, z, 0 - x))
    ors.append(lambda x, y, z: (0 - z, 0 - x, y))

    # ors.append(lambda x, y, z: (z, x, y))
    ors.append(lambda x, y, z: (y, z, x))

    # ors.append(lambda x, y, z: (z, 0 - y, x))
    ors.append(lambda x, y, z: (z, 0 - y, x))

    # ors.append(lambda x, y, z: (z, y, 0 - x))
    ors.append(lambda x, y, z: (0 - z, y, x))

    # ors.append(lambda x, y, z: (z, 0 - x, 0 - y))
    ors.append(lambda x, y, z: (0 - y, 0 - z, x))

    # ors.append(lambda x, y, z: (0 - z, 0 - y, 0 - x))
    ors.append(lambda x, y, z: (0 - z, 0 - y, 0 - x))

    # ors.append(lambda x, y, z: (0 - z, y, x))
    ors.append(lambda x, y, z: (z, y, 0 - x))

    # ors.append(lambda x, y, z: (0 - z, 0 - x, y))
    ors.append(lambda x, y, z: (0 - y, z, 0 - x))

    # ors.append(lambda x, y, z: (0 - z, x, 0 - y))
    ors.append(lambda x, y, z: (y, 0 - z, 0 - x))
    return ors


def find_match(i, j, scanners, res, scanner_found):
    scanner1 = scanners[i]
    scanner2 = scanners[j]
    for o in orientations(j, scanner_found):
        diffs = defaultdict(list)
        for b1 in scanner1:
            for b2 in scanner2:
                b2_new = o(b2[0], b2[1], b2[2])
                diffs[(b1[0] - b2_new[0], b1[1] - b2_new[1],
                       b1[2] - b2_new[2])].append((b1, b2))

        max_diff = max(diffs.items(), key=lambda x: len(x[1]))
        if len(max_diff[1]) > 11:
            print("match {} and {}".format(i, j))
            or_dict[j] = [o]
            temp = set()
            x, y, z = max_diff[0]
            for b in scanner2:
                b_new = o(b[0], b[1], b[2])
                x1 = x + b_new[0]
                y1 = y + b_new[1]
                z1 = z + b_new[2]
                res.add((x1, y1, z1))
                temp.add((x1, y1, z1))
            temp.update(scanner1)
            scanners[i] = list(temp)
            scanners[j] = list(temp)
            return max_diff
    return None


res = set()
res.update(scanners[0])


scanner_found = dict()
scanner_found[0] = (0, 0, 0)

while len(scanner_found) < len(scanners):
    for i in range(len(scanners) - 1):
        for j in range(i, len(scanners)):

            if i == j or j in scanner_found or i not in scanner_found:
                continue
            print("trying {} and {}".format(i, j))
            result = find_match(i, j, scanners, res, scanner_found)
            if result and len(result[1]) > 11:
                print("{} and {} have {} matches".format(i, j, len(result[1])))
                scanner_found[j] = result[0]


l = list(scanner_found.values())
l.sort(key=lambda x: x[0])


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


distances = []
for i in range(0, len(l) - 1):
    for j in range(i, len(l)):
        distances.append(distance(l[i], l[j]))

print(max(distances))
