import math

route_dict = {}
with open('2023/day8/input.txt') as file:
    directions = file.readline().strip()
    print(directions)
    for line in file.readlines():
        if len(line) > 1:
            origin, locations = line.strip().split(' = ')
            route_dict[origin] = locations.strip('()').split(', ')

solution_found = False
current_location = 'AAA'
list_index = 0
while not solution_found:
    current_location = route_dict[current_location][int(
        directions[list_index % len(directions)] == 'R')]
    if current_location == 'ZZZ':
        print(list_index + 1)
        break
    list_index += 1

# Part 2
route_dict = {}
with open('2023/day8/input.txt') as file:
    directions = file.readline().strip()
    print(directions)
    for line in file.readlines():
        if len(line) > 1:
            origin, locations = line.strip().split(' = ')
            route_dict[origin] = locations.strip('()').split(', ')

solution_list = []
current_locations = [item for item in route_dict.keys() if item[-1] == 'A']
for location in current_locations:
    solution_found = False
    list_index = 0
    while not solution_found:
        location = route_dict[location][int(
            directions[list_index % len(directions)] == 'R')]
        if location.endswith('Z'):
            solution_list.append(list_index + 1)
            break
        list_index += 1

print(math.lcm(solution_list[0], solution_list[1], solution_list[2],
         solution_list[3], solution_list[4], solution_list[5]))
