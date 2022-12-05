
counter = 0
counter2 = 0
with open('2022/day4/input.txt') as file:
    for line in file.readlines():
        elf1, elf2 = line.split(',')
        elf1 = set(range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1))
        elf2 = set(range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1))

        if elf1 - elf2 == set() or elf2 - elf1 == set():
            counter += 1


        if len(elf1.intersection(elf2)) > 0:
            counter2 += 1
            print(elf1)
            print(elf2)
            print(counter2)

print(counter)
print(counter2)