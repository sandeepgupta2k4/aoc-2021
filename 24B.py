with open("input.txt") as fp:
    commands = []
    for line in fp:
        row = line.strip("\n")
        res = row.split(" ")
        if res[0] == 'inp':
            commands.append((res[0], res[1]))
        else:
            commands.append((res[0], res[1], res[2]))

print(commands)
vals = dict()
vals['x'] = 0
vals['y'] = 0
vals['z'] = 0
vals['w'] = 0


def process(command, num):

    if command[0] == 'inp':
        if not num:
            return False
        vals[command[1]] = num.pop(0)
    else:
        if command[2].isdigit() or command[2].startswith("-"):
            val = int(command[2])
        else:
            val = int(vals[command[2]])

        # print("{} {} {}".format(command, vals[command[1]], val))
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
    return True


def accepted(num, commands):
    for command in commands:
        ret = process(command, num)
        if not ret:
            return False
    return True


high = 99999999999999
low = 98888888888888
val_vals = []
# num = 99999999999999
while low <= high:
    print("{} {}".format(high, low))
    num = int((low + high) / 2)
    if '0' in str(num):
        low += 2
        # num -= 1
        print("Skipping {}".format(str(num)))
        continue
    digits = list(str(num))
    print("Trying {}".format(str(num)))
    if accepted(digits, commands) and vals['z'] == 0:
        print(num)
        val_vals.append(num)
        low = num + 1
        break
    else:
        high = num - 1
        print("not valid")
    num -= 1
