with open('day10/input.txt') as file:
    data = file.readlines()

# A syntax error is closing an outer statement while the inner statement isn't
# closed yet. This basically means that a checker should keep track of all opening
# statements and their location, and validate for every closing statement which
# statement it closes, and if there is a statement inside this statement that
# needs to be closed first

# part 1

score = 0
score_dict = {'}': 1197, ']': 57, ')': 3, '>': 25137}
matches_dict = {'}': '{', ']': '[', ')': '(', '>': '<'}
incorrect_ones = []

for number, test in enumerate(data):
    status_dict = {}
    for index, character in enumerate(test):
        match = False
        status_dict[index] = False

        if character in [']', '}', ')', '>']:
            matches_to = matches_dict.get(character, '')
            # print(matches_to, character)
            for index2 in range(index - 1, -1, -1):
                # print(index2, matches_to, test[index2], test[index2] == matches_to, status_dict[index2] == False)
                if test[index2] == matches_to and status_dict[index2] == False:
                    status_dict[index] = True
                    status_dict[index2] = True
                    match = True
                    break
                elif status_dict[index2] == False and test[index2] in ['[', '{', '(', '<']:
                    break

            if not match:
                print(f'No match found for {character} at index {index} for number {number}')
                score += score_dict[character]
                incorrect_ones.append(index)
                break

print(score)

# Part 2
incomplete_ones = []
for i in range(len(data)):
    if i not in incorrect_ones:
        incomplete_ones.append(data[i])

print(len(incomplete_ones))