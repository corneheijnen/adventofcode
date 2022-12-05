crate_configuration = {index: [] for index in range(1, 10)}

with open('2022/day5/input.txt') as file:
    for line in file.readlines():

        # Build starting position
        if line[0] == '[':
            for stack in crate_configuration.keys():
                crate = line[stack * 4 - 3]
                if crate != ' ':
                    crate_configuration[stack].append(crate)

        # Peform moves
        if line[0] == 'm':
            _, amount, _, from_stack, _, to_stack = line.split(' ')

            # Make the switch
            to_move = crate_configuration[int(from_stack)][:int(amount)]
            crate_configuration[int(from_stack)] = crate_configuration[int(
                from_stack)][int(amount):]
            # to_move.reverse()
            crate_configuration[int(to_stack)] = to_move + crate_configuration[int(to_stack)]

for stack, crates in crate_configuration.items():
    print(crates[0])