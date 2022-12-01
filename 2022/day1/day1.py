
# initiate list to keep track of all calories per elf
elf_calorie_list = []

# Open file to read line by line
with open('2022/day1/input.txt') as file:
    calories_current_elf = 0  # initiate counter of caloreis current elf
    for line in file.readlines():
        if line == '\n':  # use empty line to stop algorithm
            elf_calorie_list.append(calories_current_elf)  # add to list once done
            calories_current_elf = 0  # put back to 0 again
        else:
            calories_current_elf += int(line)

print(sorted(elf_calorie_list)[-1])  # answer part 1
print(sum(sorted(elf_calorie_list)[-3:]))  # answer part 2