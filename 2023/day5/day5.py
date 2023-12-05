mappings = []
mapping_dict_dict = {}
with open('2023/day5/input.txt') as file:
    current_mapping = ''
    for line in file.readlines():
        print(line)
        if line.startswith('seeds'):
            input_list = [int(item) for item in line.split(': ')[1].strip('\n').split(' ')]
        elif line[0].isalpha():
            current_mapping = line.strip(':\n')
            mapping_dict_dict[current_mapping] = {}
            mappings.append(current_mapping)
        elif line[0].isnumeric():
            destination_range_start, source_range_start, range_length = line.strip(
                '\n').split(' ')
            destination_list = list(
                range(int(destination_range_start),
                      int(destination_range_start) + int(range_length)))
            source_list = list(
                range(int(source_range_start),
                      int(source_range_start) + int(range_length)))
            mapping_dict_dict[current_mapping] = {
                **dict(zip(source_list, destination_list)),
                **mapping_dict_dict[current_mapping]
            }

for mapping in mappings:
    print(mapping, input_list)
    output_list = []
    for item in input_list:
        output_list.append(mapping_dict_dict[mapping].get(item, item))
    input_list = output_list

print(sorted(output_list)[0])