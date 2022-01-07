with open("input.txt") as fp:
    output = []
    first = True
    for line in fp:
        row = line.strip("\n")
        if first:
            first = False
        elif not row:
            continue
        else:
            output.append(row)


#############
#...........#
###D#A#D#C###
  #D#C#B#A#
  #D#B#A#C#
  #B#C#B#A#
  #########

slot_1 = ['B', 'D', 'D', 'D']
slot_2 = ['C', 'B', 'C', 'A']
slot_3 = ['B', 'A', 'B', 'D']
slot_4 = ['A', 'C', 'A', 'C']
hall = ['.' for i in range[11]]
