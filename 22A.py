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

on_cubes = set()
i = 0
for command in commands:
    command, min_x, max_x, min_y, max_y, min_z, max_z = command
    if min_x < -50:
        min_x = -50
    if max_x > 50:
        max_x = 50

    if min_y < -50:
        min_y = -50
    if max_y > 50:
        max_y = 50

    if min_z < -50:
        min_z = -50
    if max_z > 50:
        max_z = 50

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                # if x > -51 and x < 51 and y > -51 and y < 51 and z > -51 and z < 51:
                if command == 'on':
                    on_cubes.add((x, y, z))
                else:
                    if (x, y, z) in on_cubes:
                        on_cubes.remove((x, y, z))
print(len(on_cubes))
