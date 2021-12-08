
fish_list = [1,4,1,1,1,1,1,1,1,4,3,1,1,3,5,1,5,3,2,1,1,2,3,1,1,5,3,1,5,1,1,2,1,2,1,1,3,1,5,1,1,1,3,1,1,1,1,1,1,4,5,3,1,1,1,1,1,1,2,1,1,1,1,4,4,4,1,1,1,1,5,1,2,4,1,1,4,1,2,1,1,1,2,1,5,1,1,1,3,4,1,1,1,3,2,1,1,1,4,1,1,1,5,1,1,4,1,1,2,1,4,1,1,1,3,1,1,1,1,1,3,1,3,1,1,2,1,4,1,1,1,1,3,1,1,1,1,1,1,2,1,3,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,5,1,1,1,2,2,1,1,3,5,1,1,1,1,3,1,3,3,1,1,1,1,3,5,2,1,1,1,1,5,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,5,1,4,3,3,1,3,4,1,1,1,1,1,1,1,1,1,1,4,3,5,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,1,4,4,1,1,1,1,1,1,1,5,1,1,2,5,1,1,4,1,3,1,1]
# fish_list = [3,4,3,1,2]

for iterations in range(80):
    print(iterations)
    babys = 0
    for idx, fish in enumerate(fish_list):
        # Create new fish if it reached 0

        fish -= 1
        if fish == -1:
            babys += 1
            fish = 6
        fish_list[idx] = fish

    fish_list = fish_list + [8] * babys

    len(fish_list)


# Part 2

# fish_list = [1,4,1,1,1,1,1,1,1,4,3,1,1,3,5,1,5,3,2,1,1,2,3,1,1,5,3,1,5,1,1,2,1,2,1,1,3,1,5,1,1,1,3,1,1,1,1,1,1,4,5,3,1,1,1,1,1,1,2,1,1,1,1,4,4,4,1,1,1,1,5,1,2,4,1,1,4,1,2,1,1,1,2,1,5,1,1,1,3,4,1,1,1,3,2,1,1,1,4,1,1,1,5,1,1,4,1,1,2,1,4,1,1,1,3,1,1,1,1,1,3,1,3,1,1,2,1,4,1,1,1,1,3,1,1,1,1,1,1,2,1,3,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,5,1,1,1,2,2,1,1,3,5,1,1,1,1,3,1,3,3,1,1,1,1,3,5,2,1,1,1,1,5,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,5,1,4,3,3,1,3,4,1,1,1,1,1,1,1,1,1,1,4,3,5,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,1,4,4,1,1,1,1,1,1,1,5,1,1,2,5,1,1,4,1,3,1,1]
for iterations in range(80):
    old_size = len(fish_list)
    babys = 0
    for idx, fish in enumerate(fish_list):
        # Create new fish if it reached 0

        fish -= 1
        if fish == -1:
            babys += 1
            fish = 6
        fish_list[idx] = fish

    fish_list = fish_list + [8] * babys
    print(len(fish_list), babys, len(fish_list)/old_size)

"""
F(x) = F(x-1) + B(x-1)
F(x) = F(x-2) + B(x-1) + B(x-2)
F(x) = F(x-3) + B(x-1) + B(x-2) + B(x-3)
F(x) = F(x-4) + B(x-1) + B(x-2) + B(x-3) + B(x-4)
F(x) = F(x-5) + B(x-1) + B(x-2) + B(x-3) + B(x-4) + B(x-5)
F(x) = F(x-6) + B(x-1) + B(x-2) + B(x-3) + B(x-4) + B(x-5) + B(x-6)


68 = 63 + 5
68 = 61 + 2 + 5
68 = 60 + 1 + 2 + 5
68 = 55 + 5 + 1 + 2 + 5
68 = 51 + 4 + 5 + 1 + 2 + 5
68 = 43 + 8 + 4 + 5 + 1 + 2 + 5

B(x) = B(x-7) + B(x-9)


"""

population_list = [len(fish_list)]
for i in range(256):
    if i < 8:
        babys = fish_list.count(i)
    else:
        babys = baby_list[i - 7] + baby_list[i - 9]
    population_list.append(population_list[i-1] + babys)

print(population_list[255])