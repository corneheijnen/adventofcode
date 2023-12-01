total = 0

mapping = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

with open('2023/day1/input.txt') as file:
    for line in file.readlines():

        # Comment out for part 2
        for k, v in mapping.items():
            if k in line:
                line = line.replace(k, str(v))
        line_list = list(line)
        line_digit_list = [value for value in line_list if value.isnumeric()]
        value = int(line_digit_list[0] + line_digit_list[-1])
        total += value

print(total)
