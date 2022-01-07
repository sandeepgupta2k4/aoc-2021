with open("input.txt") as fp:
    lines = []
    for line in fp:
        row = line.strip("\n")
hex_map = dict()
hex_map["0"] = "0000"
hex_map["1"] = "0001"
hex_map["2"] = "0010"
hex_map["3"] = "0011"
hex_map["4"] = "0100"
hex_map["5"] = "0101"
hex_map["6"] = "0110"
hex_map["7"] = "0111"
hex_map["8"] = "1000"
hex_map["9"] = "1001"
hex_map["A"] = "1010"
hex_map["B"] = "1011"
hex_map["C"] = "1100"
hex_map["D"] = "1101"
hex_map["E"] = "1110"
hex_map["F"] = "1111"

bin_data = ""
for char in row:
    bin_data += hex_map[char]


def handle_literal(bin_data, i):
    num = ""
    prefix = bin_data[i]
    i += 1
    while prefix == "1":
        val = bin_data[i:i+4]
        num += val
        i += 4
        prefix = bin_data[i]
        i += 1
    num += bin_data[i:i+4]
    i += 4
    return int(num, 2), i


versions = []
final_value = 0


def process_packet(bin_data, current_i):
    version = int(bin_data[current_i:current_i+3], 2)
    print("version {}".format(version))
    versions.append(version)
    current_i += 3
    type_id = int(bin_data[current_i:current_i+3], 2)
    current_i += 3
    if type_id == 4:
        value, current_i = handle_literal(bin_data, current_i)
        print(value)
        print(current_i)
        final_value = value
    else:
        len_type_id = int(bin_data[current_i], 2)
        current_i += 1
        values = []
        if len_type_id == 0:
            total_bits_len = int(bin_data[current_i: current_i+15], 2)
            current_i += 15
            last_index = current_i + total_bits_len

            while current_i < last_index:
                current_i, value = process_packet(bin_data, current_i)
                values.append(value)
        elif len_type_id == 1:
            sub_packets = int(bin_data[current_i: current_i+11], 2)
            current_i += 11
            for i in range(sub_packets):
                current_i, value = process_packet(bin_data, current_i)
                values.append(value)
        if type_id == 0:
            final_value = sum(values)
        elif type_id == 1:
            prod = 1
            for v in values:
                prod *= v
            final_value = prod
        elif type_id == 2:
            final_value = min(values)
        elif type_id == 3:
            final_value = max(values)
        elif type_id == 5:
            if values[0] > values[1]:
                final_value = 1
            else:
                final_value = 0
        elif type_id == 6:
            if values[0] < values[1]:
                final_value = 1
            else:
                final_value = 0
        elif type_id == 7:
            if values[0] == values[1]:
                final_value = 1
            else:
                final_value = 0
    return current_i, final_value


print(bin_data)
_, val = process_packet(bin_data, 0)
print(versions)
print(sum(versions))
print(val)
