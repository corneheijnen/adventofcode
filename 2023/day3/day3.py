# import re
#
# # Part 1
# grid = []
# is_symbol_grid = []
# numbers_dict = {}
# with open('2023/day3/input.txt') as file:
#     for line in file.readlines():
#         grid.append(list(line.strip('\n')))
#         is_symbol_grid.append([
#             re.fullmatch(r'[^\d.]', item) != None
#             for item in list(line.strip('\n'))
#         ])
#         numbers_dict = re.findall(r'(?<!\d)\d+(?!\d)', line.strip('\n'))
#
# total_sum = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j].isnumeric() and (j == 0
#                                        or not grid[i][j - 1].isnumeric()):
#             neighbouring_symbol = False
#             number = grid[i][j]
#             for k in range(-1, 2):
#                 for l in range(-1, 2):
#                     try:
#                         if is_symbol_grid[i + k][j + l]:
#                             neighbouring_symbol = True
#                     except IndexError:
#                         continue
#             while grid[i][j + 1].isnumeric():
#                 j += 1
#                 number += grid[i][j]
#                 for k in range(-1, 2):
#                     for l in range(-1, 2):
#                         try:
#                             if is_symbol_grid[i + k][j + l]:
#                                 neighbouring_symbol = True
#                         except IndexError:
#                             continue
#                 if j + 1 >= len(grid[i]):
#                     break
#             if neighbouring_symbol:
#                 print(f"{int(number)} added")
#                 total_sum += int(number)
#             else:
#                 print(f"{int(number)} not added")
#
# print(total_sum)


# Part 2
grid = []
is_gear_grid = []
gear_list = []
with open('2023/day3/input.txt') as file:
    for line in file.readlines():
        grid.append(list(line.strip('\n')))

total_sum = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '*':
            surrounding_numbers = list()
            used_coordinates = set()
            count_numbers = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    new_coordinates = set()
                    if grid[i + k][j + l].isnumeric():
                        part_of_number = ''
                        m = 0
                        while grid[i + k][j + l + m].isnumeric():
                            part_of_number += grid[i + k][j + l + m]
                            new_coordinates.add(str([i + k, j + l + m]))
                            if j + l + m + 2 <= len(grid[i]):
                                m += 1
                            else:
                                break
                        if j + l > 0:
                            n = -1
                            while grid[i + k][j + l + n].isnumeric():
                                part_of_number = grid[i + k][j + l + n] + part_of_number
                                new_coordinates.add(str([i + k, j + l + n]))
                                if j + l + n - 1 >= 0:
                                    n -= 1
                                else:
                                    break
                        if not new_coordinates & used_coordinates:
                            surrounding_numbers.append(part_of_number)
                            used_coordinates = used_coordinates.union(new_coordinates)
                        else:
                            continue
            if len(surrounding_numbers) == 2:
                print(surrounding_numbers)
                surrounding_numbers_list = list(surrounding_numbers)
                total_sum += int(surrounding_numbers_list[0]) * int(surrounding_numbers_list[1])
                print(total_sum)
