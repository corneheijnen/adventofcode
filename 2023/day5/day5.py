mappings = []
mapping_dict_dict = {}
with open('2023/day5/input.txt') as file:
    current_mapping = ''
    for line in file.readlines():
        if line.startswith('seeds'):
            input_list = [
                int(item)
                for item in line.split(': ')[1].strip('\n').split(' ')
            ]
        elif line[0].isalpha():
            current_mapping = line.strip(':\n')
            mapping_dict_dict[current_mapping] = {}
            mappings.append(current_mapping)
        elif line[0].isnumeric():
            destination_range_start, source_range_start, range_length = line.strip(
                '\n').split(' ')
            source_range_end = int(source_range_start) + int(range_length)
            delta = int(destination_range_start) - int(source_range_start)
            mapping_dict_dict[current_mapping][source_range_start] = [
                int(source_range_start), source_range_end, delta
            ]

print(input_list)
for mapping in mappings:
    output_list = []
    for item in input_list:
        match = False
        for k, v in mapping_dict_dict[mapping].items():
            if mapping_dict_dict[mapping][k][0] <= item < mapping_dict_dict[
                    mapping][k][1]:
                output_list.append(item + mapping_dict_dict[mapping][k][2])
                match = True
                break
        if not match:
            # print(f"No match found for item {item}")
            output_list.append(item)
    input_list = output_list
    print(output_list)

print(sorted(output_list)[0])
