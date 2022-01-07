with open("input.txt") as fp:
    commands = []
    for line in fp:
        row = line.strip("\n")
        command, cors = row.split(" ")
        x, y, z = cors.split(",")
        _, range_x = x.split("=")
        min_x, max_x = range_x.split("..")

        _, range_y = y.split("=")
        min_y, max_y = range_y.split("..")

        _, range_z = z.split("=")
        min_z, max_z = range_z.split("..")

        commands.append((command, int(min_x), int(max_x), int(
            min_y), int(max_y), int(min_z), int(max_z)))


def count(command):
    _, min_x, max_x, min_y, max_y, min_z, max_z = command
    return (max_x - min_x + 1) * (max_y - min_y + 1) * (max_z - min_z + 1)


def add_to_list(intervals, command):
    if command[0] == 'on':
        intervals.append(command)


def get_updated(command, min_val, max_val, dim):
    temp = list(command)
    temp[dim] = min_val
    temp[dim + 1] = max_val
    return tuple(temp)


def process(command1, command2, intervals, dim):
    # print("{} {} {} {}".format(command1, command2, intervals, dim))
    if dim > 5:
        add_to_list(intervals, command2)
        return intervals

    min_x1 = command1[dim]
    max_x1 = command1[dim + 1]
    min_x2 = command2[dim]
    max_x2 = command2[dim + 1]

    if min_x1 < min_x2:
        if max_x1 < min_x2:
            add_to_list(intervals, command1)
            add_to_list(intervals, command2)
            return intervals
        else:
            if max_x1 < max_x2:
                add_to_list(intervals, get_updated(
                    command1, min_x1, min_x2 - 1, dim))
                # intervals.append(
                #     (com1, min_x1, min_x2 - 1, min_y1, max_y1, min_z1, max_z1))
                add_to_list(intervals, get_updated(
                    command2, max_x1 + 1, max_x2, dim))
                # intervals.append((com2, max_x1 + 1, max_x2, min_y2, max_y2, min_z2, max_z2))

                return process(get_updated(command1, min_x2, max_x1, dim), get_updated(command2, min_x2, max_x1, dim), intervals, dim)

            elif max_x1 > max_x2:
                add_to_list(intervals, get_updated(
                    command1, min_x1, min_x2 - 1, dim))
                add_to_list(intervals, get_updated(
                    command1, max_x2 + 1, max_x1, dim))
                return process(get_updated(command1, min_x2, max_x2, dim), get_updated(command2, min_x2, max_x2, dim), intervals, dim)
            else:
                add_to_list(intervals, get_updated(
                    command1, min_x1, min_x2 - 1, dim))
                return process(get_updated(command1, min_x2, max_x2, dim), get_updated(command2, min_x2, max_x2, dim), intervals, dim)
    elif min_x1 > min_x2:
        if min_x1 > max_x2:
            add_to_list(intervals, command1)
            add_to_list(intervals, command2)
            return intervals
        else:
            if max_x1 < max_x2:
                add_to_list(intervals, get_updated(
                    command2, min_x2, min_x1 - 1, dim))
                add_to_list(intervals, get_updated(
                    command2, max_x1 + 1, max_x2, dim))
                return process(get_updated(command1, min_x1, max_x1, dim), get_updated(command2, min_x1, max_x1, dim), intervals, dim)
            elif max_x1 > max_x2:
                add_to_list(intervals, get_updated(
                    command1, max_x2 + 1, max_x1, dim))
                add_to_list(intervals, get_updated(
                    command2, min_x2, min_x1 - 1, dim))
                return process(get_updated(command1, min_x1, max_x2, dim), get_updated(command2, min_x1, max_x2, dim), intervals, dim)
            else:
                add_to_list(intervals, get_updated(
                    command2, min_x2, min_x1 - 1, dim))
                return process(get_updated(command1, min_x1, max_x2, dim), get_updated(command2, min_x1, max_x2, dim), intervals, dim)
    elif min_x1 == min_x2:
        if max_x1 < max_x2:
            add_to_list(intervals, get_updated(
                command2, max_x1 + 1, max_x2, dim))
            return process(get_updated(command1, min_x2, max_x1, dim), get_updated(command2, min_x2, max_x1, dim), intervals, dim)
        elif max_x1 > max_x2:
            add_to_list(intervals, get_updated(
                command1, max_x2 + 1, max_x1, dim))
            return process(get_updated(command1, min_x1, max_x2, dim), get_updated(command2, min_x1, max_x2, dim), intervals, dim)
        else:
            return process(command1, command2, intervals, dim + 2)


def find_common(command1, command2, dim):
    # print("{} {} {} {}".format(command1, command2, intervals, dim))
    if dim > 5:
        return command1

    min_x1 = command1[dim]
    max_x1 = command1[dim + 1]
    min_x2 = command2[dim]
    max_x2 = command2[dim + 1]

    if min_x1 < min_x2:
        if max_x1 < min_x2:
            return None
        else:
            if max_x1 < max_x2:
                return find_common(get_updated(command1, min_x2, max_x1, dim), get_updated(command2, min_x2, max_x1, dim), dim)

            elif max_x1 > max_x2:
                return find_common(get_updated(command1, min_x2, max_x2, dim), get_updated(command2, min_x2, max_x2, dim), dim)
            else:
                return find_common(get_updated(command1, min_x2, max_x2, dim), get_updated(command2, min_x2, max_x2, dim), dim)
    elif min_x1 > min_x2:
        if min_x1 > max_x2:
            return None
        else:
            if max_x1 < max_x2:
                return find_common(get_updated(command1, min_x1, max_x1, dim), get_updated(command2, min_x1, max_x1, dim), dim)
            elif max_x1 > max_x2:
                return find_common(get_updated(command1, min_x1, max_x2, dim), get_updated(command2, min_x1, max_x2, dim), dim)
            else:
                return find_common(get_updated(command1, min_x1, max_x2, dim), get_updated(command2, min_x1, max_x2, dim), dim)
    elif min_x1 == min_x2:
        if max_x1 < max_x2:
            return find_common(get_updated(command1, min_x2, max_x1, dim), get_updated(command2, min_x2, max_x1, dim), dim)
        elif max_x1 > max_x2:
            return find_common(get_updated(command1, min_x1, max_x2, dim), get_updated(command2, min_x1, max_x2, dim), dim)
        else:
            return find_common(command1, command2, dim + 2)


result = []
result.append((commands[0], True))
for i in range(1, len(commands)):
    command = commands[i]
    temp_list = []
    for c in result:
        com = c[0]
        t = find_common(com, command, 1)
        if t:
            temp = (t, not c[1])
            temp_list.append(temp)
    result.extend(temp_list)
    if command[0] == 'on':
        result.append((command, True))

total = 0
for command in result:
    if command[1]:
        total += count(command[0])
    else:
        total -= count(command[0])
print(total)
