from typing import List, Set


def translate_character_list_into_priority_set(compartment_list: List[str]):
    priority_set = [
        ord(item) - 96 if item.islower() else ord(item) - 38
        for item in compartment_list
    ]
    print(priority_set)
    return set(priority_set)


class RuckSackConfiguration():

    def __init__(self, input: str):
        self.first_compartment = list(input)[:int(len(input) / 2)]
        self.second_compartment = list(input)[int(len(input) / 2):]

    def calculate_priority_sum(self):
        first_compartment = translate_character_list_into_priority_set(
            self.first_compartment)
        second_compartment = translate_character_list_into_priority_set(
            self.second_compartment)

        intersection = first_compartment.intersection(second_compartment)
        print(intersection)

        return sum(intersection)


total_sum = 0
with open('2022/day3/input.txt') as file:
    for line in file.readlines():

        rucksack_configuration = RuckSackConfiguration(line[:-1])
        print(rucksack_configuration.first_compartment)
        print(rucksack_configuration.second_compartment)
        priority_sum = rucksack_configuration.calculate_priority_sum()
        total_sum += priority_sum
        print(total_sum)

##################### Part 2 ##############################


class RuckSackConfiguration2():

    def __init__(self, first_compartment: str, second_compartment: str,
                 third_compartment: str):
        self.first_compartment = list(first_compartment)
        self.second_compartment = list(second_compartment)
        self.third_compartment = list(third_compartment)

    def calculate_priority_sum(self):
        first_compartment = translate_character_list_into_priority_set(
            self.first_compartment)
        second_compartment = translate_character_list_into_priority_set(
            self.second_compartment)
        third_compartment = translate_character_list_into_priority_set(
            self.third_compartment)

        intersection = set.intersection(first_compartment, second_compartment,
                                        third_compartment)
        print(intersection)

        return sum(intersection)


total_sum = 0
with open('2022/day3/input.txt') as file:
    lines = [line[:-1] for line in file]

while len(lines) > 0:
    files_to_process = lines[:3]
    lines = lines[3:]
    rucksack_configuration = RuckSackConfiguration2(files_to_process[0],
                                                    files_to_process[1],
                                                    files_to_process[2])
    priority_sum = rucksack_configuration.calculate_priority_sum()
    total_sum += priority_sum

print(total_sum)
