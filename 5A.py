with open("input.txt") as fp:
    lines = []
    points = dict()
    for line in fp:
        row = line.strip("\n")
        l = row.split(" ")
        x1, y1 = map(int, l[0].split(","))
        x2, y2 = map(int, l[2].split(","))
        if x1 == x2 and y1 != y2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2+1):
                if (x1, i) in points:
                    points[(x1, i)] += 1
                else:
                    points[(x1, i)] = 1
        elif y1 == y2 and x1 != x2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2+1):
                if (i, y1) in points:
                    points[(i, y1)] += 1
                else:
                    points[(i, y1)] = 1
total = 0
for key in points:
    if points[key] > 1:
        total += 1

print(total)
