from collections import Counter

output_list = []
with open('day8/input.txt') as file:

    for line in file.readlines():
        output_list += line.split('|')[1].split()

answer = len([element for element in output_list if len(element) in [2, 3, 4, 7]])


# Part 2
output_list = []
with open('day8/input.txt') as file:
    output_list = file.readlines()

class Display():
    """Representation of a four digit display"""

    def __init__(self, data):
        self.inputs = sorted(data.split('|')[0].split(), key=len)
        self.outputs = data.split('|')[1].split()
        self.a = self.get_a()
        self.b = self.get_value_based_on_counter(6)
        self.c = self.get_value_based_on_counter(8, self.a)
        self.e = self.get_value_based_on_counter(4)
        self.f = self.get_value_based_on_counter(9)
        self.d = self.get_d()
        self.g = self.get_value_based_on_counter(7, self.d)
        self.mapping = {self.a: 'a', self.b: 'b', self.c: 'c', self.d: 'd', self.e: 'e', self.f: 'f', self.g: 'g',}
        self.digits = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5',
                   'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}

    def get_a(self):
        """
        function to retrieve signal that maps to a (top middle)
        This a is the signal that is in the len(3) -> 7, but not in len(2) -> 1
        It can be retrieved by sorting the inputs list and then taking the first 2
        """
        return ''.join(set(self.inputs[1]).difference(set(self.inputs[0])))


    def get_d(self):
        """get d mapping by starting out with all signals making 4 and removing those already mapped"""

        starting_point = list(self.inputs[2])
        starting_point.remove(self.b)
        starting_point.remove(self.c)
        starting_point.remove(self.f)
        return ''.join(starting_point)


    def get_value_based_on_counter(self, value, to_remove=None):
        """
        Get the number that signals for e
        This is the signal that is just used 4 times
        """
        inputs_string = ''.join(self.inputs)
        counter = Counter(inputs_string)
        if value != '':
            del counter[to_remove]
        return {v: k for k, v in counter.items()}[value]

    def analyse_input(self):
        """Do initial analysis on input signals to retrieve some mapping"""
        self.inputs = sorted(self.inputs, key=len)
        print(self.inputs)

    def get_output(self):
        digits = ''
        for output in self.outputs:
            mapping = []
            for value in output:
                mapped = self.mapping[value]
                mapping.append(mapped)
            mapping = ''.join(sorted(mapping))
            digit = self.digits[mapping]
            digits += digit

        return int(digits)

total = 0
for i in range(len(output_list)):
    print(i)
    display = Display(output_list[i])
    total += display.get_output()

print(total)