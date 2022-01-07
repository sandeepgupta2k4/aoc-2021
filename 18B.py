import math
import json
import sys
with open("input.txt") as fp:
    nums = []
    for line in fp:
        row = line.strip("\n")
        # l = json.loads(row)
        nums.append(row)

# for num in nums:
#     print(num)


def should_explode(num, level):
    if level > 3:
        return True
    for n in num:
        if type(n) is list:
            explode = should_explode(n, level + 1)
            if explode:
                return True

    return False


def should_split(num):
    for n in num:
        if type(n) is int and n > 9:
            return True
        elif type(n) is list:
            split = should_split(n)
            if split:
                return True

    return False


def split(num):
    print("split called")
    i = 0
    for n in num:
        if type(n) is int and n > 9:
            left = math.floor(n/2)
            right = math.ceil(n/2)
            num[i] = [left, right]
            return True
        elif type(n) is list:
            spl = split(n)
            if spl:
                return True
        i += 1
    return False


def add_left(num, val):
    for i in range(len(num)):
        if type(num[i]) is list:
            add_left(num[i], val)
        else:
            num[i] += val
            return


def explode(num, level, exploded):
    # print(num)
    # print(level)
    if level > 3:
        exploded.add(True)
        return True, num[0], num[1], True

    i = 0
    for n in num:
        # print(n)
        if type(n) is list and len(exploded) == 0:
            expl, left, right, orig = explode(n, level + 1, exploded)
            print(exploded)
            if expl:
                # print("expl {} {} {} {} {}".format(
                #     num, expl, n, left, right, orig, already_exploded))
                if i == 1:
                    if orig:
                        num[1] = 0
                    if left > 0:
                        if type(num[0]) is list:
                            add_left(num[0], left)
                        else:
                            num[0] += left
                    return True, 0, right, False
                elif i == 0:
                    if orig:
                        num[0] = 0
                    if right > 0:
                        if type(num[1]) is list:
                            add_left(num[1], right)
                        else:
                            num[1] += right
                    return True, left, 0, False
        if len(exploded) > 0:
            break
        i += 1
    # print("returning {}".format(len(exploded)))
    return len(exploded) > 0, 0, 0, False


# num = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
# # explode(num, 0)

# split(num)
# print(num)

def update_left_num(num, index, val):
    # print("updating left")
    # print(num)
    while index > 0:
        # print(index)
        ch = num[index]
        if ch in "0123456789":
            j = index
            remaining = num[j+1:]
            # print(remaining)
            while ch in "0123456789":
                index -= 1
                ch = num[index]
            i = index + 1
            result = num[:i] + str(int("".join(num[i:j+1])) + val) + remaining
            # print(result)
            return result
        index -= 1

    return num


def update_right_num(num, val):
    index = 0
    while index < len(num):
        ch = num[index]
        if ch in "0123456789":
            i = index
            n = 0
            while ch in "0123456789":
                index += 1
                n = (10 * n) + int(ch)
                ch = num[index]
            j = index
            updated = int(n) + int(val)
            result = num[:i] + str(updated) + num[j:]
            return result
        index += 1

    return num


def get_child(i, num):
    ch = num[i]
    s = ""
    start = i
    while ch != "]":
        if ch == "[":
            s = ch
            start = i
            i += 1
            ch = num[i]
        else:
            s += ch
            i += 1
            ch = num[i]
    return start, i, s


def explode(num):
    # k = i
    # ch = num[k]
    # comma = False
    # while ch != "]":
    #     if ch == "[":
    #         comma = True
    #         break
    #     k += 1
    #     ch = num[k]

    # if comma:
    #     i = k

    # print(i)
    # j = i
    # c = num[i]
    # val = ""
    # while c != "]":
    #     val += c
    #     j += 1
    #     c = num[j]
    # print(val)
    # left, right = map(int, val[1:].split(","))
    count = 0
    i = 0
    while i < len(num):
        char = num[i]
        if char == "[":
            count += 1
            if count == 5:
                num = explode_internal(i, num)
                exploded = True
                print("After explode = {}".format(num))
                # sys.exit(0)
                break
        elif char == "]":
            count -= 1
        i += 1


def explode_internal(i, num):
    start, end, s = get_child(i, num)
    print("{} {} {}".format(start, end, s))
    left, right = map(int, s[1:].split(","))
    # print("{} {} {} {}".format(i, j, left, right))
    return update_left_num(
        num[:start], start-1, left) + "0" + update_right_num(num[end+1:], right)


# num = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
# print(explode(num))


def reduce(num):
    print(num)
    while True:
        i = 0
        count = 0
        exploded = False
        splitted = False
        while i < len(num):
            char = num[i]
            if char == "[":
                count += 1
                if count == 5:
                    num = explode_internal(i, num)
                    exploded = True
                    print("After explode = {}".format(num))
                    # sys.exit(0)
                    break
            elif char == "]":
                count -= 1
            i += 1

        if not exploded:
            i = 0
            count = 0
            while i < len(num):
                char = num[i]
                if char in "0123456789":
                    val = ""
                    j = i
                    while char in "0123456789":
                        val += char
                        j += 1
                        char = num[j]
                    val = int(val)
                    if val > 9:
                        left = math.floor(val/2)
                        right = math.ceil(val/2)
                        replace = "[{},{}]".format(left, right)
                        num = num[:i] + replace + num[j:]
                        splitted = True
                        print("After split = {}".format(num))
                        break
                i += 1
        if not exploded and not splitted:
            break
    return num

# def add(num1, num2):
#     if not num1:
#         return num2

#     s = [num1, num2]
#     while True:
#         print("blah blah blah")
#         exploded, _, _, _ = explode(s, 0, set())
#         if not exploded:
#             print("no explode spliting")
#             print("before {}".format(s))
#             sp = split(s)
#             if not sp:
#                 print("no split")
#                 return s
#             else:
#                 print("split done")
#                 print("after{}".format(s))
#         else:
#             print("explode done")


def add(num1, num2):
    s = "[" + num1 + "," + num2 + "]"
    # print("After add = {}".format(s))
    return reduce(s)


def magnitude(num):
    if type(num) is int:
        return num
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


max_mag = 0
for i in range(0, len(nums) - 1):
    for j in range(i+1, len(nums)):
        result = add(nums[i], nums[j])
        current = magnitude(json.loads(result))
        if current > max_mag:
            max_mag = current

print(max_mag)
