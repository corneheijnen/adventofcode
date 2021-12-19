with open('day14/input.txt') as file:
    start = file.readlines(1)[0].strip()

    mapping = file.readlines()
    mapping = {row[:2] : row[-2] for row in mapping[1:]}

#Part 1
"""
epochs = 10
for epoch in range(epochs):
    print(epoch)
    new_polymer = ''
    for i in range(len(start)):

            pair = start[i:i + 2]
            element = mapping.get(pair, '')

            new_polymer += (start[i] + element)

    start = new_polymer

counter_dict = {}
for character in start:
    try:
        counter_dict[character] += 1
    except KeyError:
        counter_dict[character] = 1

minimal_value = 99999
maximum_value = 0
for key, value in counter_dict.items():
    if value > maximum_value:
        maximum_value = value
    if value < minimal_value:
        minimal_value = value

print(maximum_value - minimal_value)
"""

# Part 2
# This long polymer chain can also be seen as just a big bunch of pairs
epochs = 40
last_letter = start[-1]

# First
pairs_dict = {key: 0 for key in mapping.keys()}
mapped_dict = {key: 0 for key in mapping.keys()}

for i in range(len(start) -1):
    try:
        pairs_dict[start[i] + start[i+1]] += 1
    except KeyError:
        pairs_dict[start[i] + start[i + 1]] = 1

for epoch in range(epochs):
    mapped_dict = {key: 0 for key in mapping.keys()}

    # Loop through pairs_dict
    for key, value in pairs_dict.items():
        new_key = mapping.get(key, '')
        mapped_dict[key[0] + new_key] += value
        mapped_dict[new_key + key[1]] += value

    pairs_dict = mapped_dict

counter_dict = {}
for (character1, character2), count in pairs_dict.items():
    try:
        counter_dict[character1] += count
    except KeyError:
        counter_dict[character1] = count
counter_dict[last_letter] += 1

print(max(counter_dict.values()) - min(counter_dict.values()))