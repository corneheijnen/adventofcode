total_result = 0
with open('2023/day9/input.txt') as file:
    for line in file.readlines():
        print(line)
        input_list = line.strip().split(' ')
        input_list.reverse()
        difference_list = [-1]
        value = int(input_list[-1])
        while not all([item == 0 for item in difference_list]):
            difference_list = [
                int(input_list[i + 1]) - int(input_list[i])
                for i in range(len(input_list) - 1)
            ]
            input_list = difference_list
            # print(input_list)
            value += input_list[-1]
        total_result += value

print(total_result)