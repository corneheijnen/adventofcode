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
    print(current_location)
    if current_location == 'ZZZ':
        print(list_index + 1)
        break
    list_index += 1