from functools import reduce


def get_nested_value(output_folder, cwd, final_key, final_value):
    for directory in cwd:
        output_folder = output_folder[directory]
    output_folder[final_key] = final_value

def get_values_from_nested_dict(nested_dict):
    for keys, values in nested_dict.items():
        if isinstance(values, dict):
            yield from get_values_from_nested_dict(nested_dict[keys])
        else:
            yield keys, values

def return_as_dictionary(nested_dict):
    return dict(get_values_from_nested_dict(nested_dict))

cwd = []
output_folder = {}
with open('2022/day7/input(simple).txt') as file:
    for line in file.readlines():
        if line == '$ ls\n':
            task = 'add_folders_to_dict'
        elif line.startswith('$ cd'):
            task = 'change_directory'
            if line == '$ cd ..\n':
                cwd.pop(-1)
                print(cwd)
            elif line == '$ cd /\n':
                cwd = []
            else:
                cwd.append(line.split(' ')[-1].strip('\n'))
        else:
            if task == 'add_folders_to_dict':
                if line.startswith('dir'):
                    new_key = line.split(' ')[-1].strip('\n')
                    updates = {new_key: {}}
                    if len(cwd) == 0:
                        output_folder[new_key] = {}
                    else:
                        get_nested_value(output_folder, cwd, new_key, {})
                else:
                    new_key = line.split(' ')[1].strip('\n')
                    new_value = int(line.split(' ')[0])
                    if len(cwd) == 0:
                        output_folder[new_key] = new_value
                    else:
                        get_nested_value(output_folder, cwd, new_key, new_value)
            elif task == 'change_directory':
                print(line)

size_dict = return_as_dictionary(output_folder)

total_small_sizes = 0
for folder, size in size_dict.items():
    if size <= 100000:
        total_small_sizes += size
print(size)
