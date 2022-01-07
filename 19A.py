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


# def transform(x, scanner):
#     new = []
#     for item in scanner:
#         new.append(item + x)
#     return new


# def combinations(scanner):
#     combs = []
#     for i in range(-2000, 2001):
#         combs.append((i, transform(i, scanner)))
#     return combs


# def relative(scanner):
#     rel = []
#     for i in range(1, len(scanner)):
#         rel.append((scanner[0][0] - scanner[i][0], scanner[0]
#                     [1] - scanner[i][1], scanner[0][1] - scanner[i][1]))

#     rel.sort(key=lambda x: x[0])
#     return rel


# def find_matches(scanner1, scanner2):
#     # print("scanner1")
#     # print(scanner1)
#     # print("scanner2")
#     # print(scanner2)

#     return set(scanner1).intersection(set(scanner2))


# def orientations(b):
#     x = b[0]
#     y = b[1]
#     z = b[2]

#     ors = []
#     ors.append((x, y, z))
#     ors.append((x, z, y))
#     ors.append((y, x, z))
#     ors.append((y, z, x))
#     ors.append((z, x, y))
#     ors.append((z, y, x))

#     ors.append((x, y, 0 - z))
#     ors.append((x, z, 0 - y))
#     ors.append((y, x, 0 - z))
#     ors.append((y, z, 0 - x))
#     ors.append((z, x, 0 - y))
#     ors.append((z, y, 0 - x))

#     ors.append((x, 0 - y, z))
#     ors.append((x, 0 - z, y))
#     ors.append((y, 0 - x, z))
#     ors.append((y, 0 - z, x))
#     ors.append((z, 0 - x, y))
#     ors.append((z, 0 - y, x))

#     ors.append((0 - x, y, z))
#     ors.append((0 - x, z, y))
#     ors.append((0 - y, x, z))
#     ors.append((0 - y, z, x))
#     ors.append((0 - z, x, y))
#     ors.append((0 - z, y, x))

#     return ors


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

    #ors.append(lambda x, y, z: (x, 0 - y, 0 - z))
    ors.append(lambda x, y, z: (x, 0 - y, 0 - z))

    # ors.append(lambda x, y, z: (x, 0 - z, y))
    ors.append(lambda x, y, z: (x, z, 0 - y))

    #ors.append(lambda x, y, z: (x, z, 0 - y))
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


scanner_found = set()
scanner_found.add(0)

while len(scanner_found) < len(scanners):
    for i in range(len(scanners) - 1):
        for j in range(i, len(scanners)):

            if i == j or j in scanner_found or i not in scanner_found:
                continue
            print("trying {} and {}".format(i, j))
            result = find_match(i, j, scanners, res, scanner_found)
            if result and len(result[1]) > 11:
                print("{} and {} have {} matches".format(i, j, len(result[1])))
                scanner_found.add(j)

l = list(res)
l.sort(key=lambda x: x[0])
for m in l:
    print(m)

print(len(l))
