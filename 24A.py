import sys
with open("input.txt") as fp:
    commands = []
    for line in fp:
        row = line.strip("\n")
        res = row.split(" ")
        if res[0] == 'inp':
            commands.append((res[0], res[1]))
        else:
            commands.append((res[0], res[1], res[2]))

# print(commands)


def process(command, num, vals):
    if command[0] == 'inp':
        print("input")
        vals[command[1]] = num.pop(0)
    else:
        if command[2].isdigit() or command[2].startswith("-"):
            val = int(command[2])
        else:
            val = int(vals[command[2]])

        print("{} {} {}".format(command, vals[command[1]], val))
        if command[0] == 'add':
            vals[command[1]] += val
        elif command[0] == 'mul':
            vals[command[1]] *= val
        elif command[0] == 'div':
            if val == 0:
                return False
            vals[command[1]] = int(vals[command[1]] / val)
        elif command[0] == 'mod':
            if val == 0:
                return False
            vals[command[1]] %= val
        else:
            if vals[command[1]] == val:
                vals[command[1]] = 1
            else:
                vals[command[1]] = 0
    print(vals)
    return True


def combinations(l):
    if l == 1:
        return ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    c = combinations(l - 1)
    result = []
    for i in range(1, 10):
        for com in c:
            result.append(str(i) + str(com))
    return result


# coms = combinations(7)
# coms.sort()
# print(coms)


def get_num(com):
    result = [9]
    for c in com:
        result.append(int(c))
        result.append(9)
    return result


def accepted(num, commands):
    vals = dict()
    vals['x'] = 0
    vals['y'] = 0
    vals['z'] = 0
    vals['w'] = 0
    # num = [6, 9, 9, 1, 4, 9, 9, 9, 9, 7, 5, 3, 6, 9]
    num = [1, 4, 9, 1, 1, 6, 7, 5, 3, 1, 1, 1, 1, 4]
    for z in range(14):
        for j in range(18):
            command = commands[(18 * z) + j]
            process(command, [num[z]], vals)
    temp_dict = vals.copy()
    print(temp_dict)
    # for k in range(9, 0, -1):
    #     first = temp_dict.copy()
    #     for j in range(18):
    #         command = commands[(18 * 10) + j]
    #         process(command, [k], first)
    #     for l in range(9, 0, -1):
    #         second = first.copy()
    #         for j in range(18):
    #             command = commands[(18 * 11) + j]
    #             process(command, [l], second)
    #         for m in range(9, 0, -1):
    #             third = second.copy()
    #             for j in range(18):
    #                 command = commands[(18 * 12) + j]
    #                 process(command, [m], third)
    #             for n in range(9, 0, -1):
    #                 fourth = third.copy()
    #                 for j in range(18):
    #                     command = commands[(18 * 13) + j]
    #                     process(command, [n], fourth)
    #                 if fourth['z'] == 0:
    #                     print("9991499999, {} {} {} {} {}".format(
    #                         k, l, m, n, fourth))
    #                     sys.exit(0)

    #     sys.exit(0)
    # if fourth['z'] == 0:
    #


# def accepted(num, commands):
#     vals = dict()
#     vals['x'] = 0
#     vals['y'] = 0
#     vals['z'] = 0
#     vals['w'] = 0
#     for command in commands:
#         ret = process(command, num, vals)
#         if not ret:
#             return False, vals
#     return True, vals


# for num in coms:
#     print("Trying {}".format(num))
#     digits = get_num(num)
#     finish, vals = accepted(digits, commands)
#     print(vals)
#     if vals['z'] == 0:
#         print(digits)
#         break
# num = list(str(99914999979794))
accepted(None, commands)

# while True:
#     if '0' in str(num):
#         num -= 1
#         print("Skipping {}".format(str(num)))
#         continue
#     digits = list(str(num))
#     print("Trying {}".format(str(num)))
#     if accepted(digits, commands) and vals['z'] == 0:
#         print(num)
#         break
#     else:
#         print("not valid")
#     print(vals)
#     num -= 1
#     break
