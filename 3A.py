with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
        lines.append(row)


numbers1 = list(lines)
numbers2 = list(lines)
result = []
eps = []

for i in range(len(lines[0])):
    zeros = 0
    ones = 0
    for j in range(len(numbers1)):
        if numbers1[j][i] == '0':
            zeros += 1
        else:
            ones += 1
    temp1 = set()
    temp2 = set()
    for num in numbers1:
        if ones >= zeros:
            if num[i] == '1':
                temp1.add(num)
        else:
            if num[i] == '0':
                temp1.add(num)
    numbers1 = list(temp1)

print(numbers1)


for i in range(len(lines[0])):
    zeros = 0
    ones = 0
    for j in range(len(numbers2)):
        if numbers2[j][i] == '0':
            zeros += 1
        else:
            ones += 1

    temp1 = set()
    for num in numbers2:
        if zeros <= ones:
            if num[i] == '0':
                temp1.add(num)
        else:
            if num[i] == '1':
                temp1.add(num)
    # print(numbers2)
    numbers2 = list(temp1)
    if len(numbers2) == 1:
        break
print(numbers2)
co2 = int("".join(numbers2), 2)
oxy = int("".join(numbers1), 2)

print(co2 * oxy)
