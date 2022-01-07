def step(x, y, pos_x, pos_y):
    pos_x += x
    pos_y += y
    if x > 0:
        x -= 1
    elif x < 0:
        x += 1

    y -= 1
    return pos_x, pos_y, x, y


def in_target(x, y):
    target_min_x = 257
    target_max_x = 286
    target_min_y = -101
    target_max_y = -57
    return x >= target_min_x and x <= target_max_x and y >= target_min_y and y <= target_max_y


def missed(x, y):
    target_max_x = 286
    target_min_y = -101
    return y < target_min_y or x > target_max_x


def hits(x, y):
    max_y = 0
    pos_x = 0
    pos_y = 0
    while not in_target(pos_x, pos_y):
        if missed(pos_x, pos_y):
            return False, 0
        pos_x, pos_y, x, y = step(x, y, pos_x, pos_y)
        if pos_y > max_y:
            max_y = pos_y
    return True, max_y


max_y = 0
sx = 0
sy = 0
options = []
for i in range(1, 1000):
    for j in range(-1000, 1000):
        h, my = hits(i, j)
        if h:
            if my > max_y:
                max_y = my
                sx = i
                sy = j
            options.append((max_y, sx, sy))

print("{} {} {}".format(sx, sy, max_y))
print(len(options))
