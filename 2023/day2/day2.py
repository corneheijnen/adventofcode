import re


class Reveals:

    def __init__(self, input_string: str):
        self.blue = self._get_number_of_colxor('blue', input_string)
        self.red = self._get_number_of_colxor('red', input_string)
        self.green = self._get_number_of_colxor('green', input_string)

    def _get_number_of_colxor(self, color: str, input_string: str):
        match = re.search(f'\d*(?=\s{color})', input_string)
        if match:
            return int(input_string[match.start():match.end()])
        else:
            return 0

    def is_reveal_within_numbers(self):
        if self.blue <= 14 and self.red <= 12 and self.green <= 13:
            return True
        else:
            return False


# Part 1
incorrect_ids = set()
all_ids = set()
with open('2023/day2/input.txt') as file:
    for line in file.readlines():
        id_number, shows = line.split(':')
        id_number = int(id_number.split(' ')[1])
        all_ids.add(id_number)
        shows_list = shows.split(';')
        for reveal in shows_list:
            instance = Reveals(reveal)
            if not instance.is_reveal_within_numbers():
                incorrect_ids.add(id_number)

correct_ids = all_ids.difference(incorrect_ids)
print(sum(correct_ids))

# Part 2
total_value = 0
with open('2023/day2/input.txt') as file:
    for line in file.readlines():
        _, shows = line.split(':')
        reveals = [Reveals(reveal) for reveal in shows.split(';')]
        product = max([reveal.red for reveal in reveals]) * max(
            [reveal.green
             for reveal in reveals]) * max([reveal.blue for reveal in reveals])
        total_value += product

print(total_value)
