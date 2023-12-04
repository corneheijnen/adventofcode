# part 1
score = 0
with open('2023/day4/input.txt') as file:
    for line in file.readlines():
        winnning_numbers, your_numbers = line.strip('\n').split(' | ')
        winnning_numbers_set = set(
            winnning_numbers.split(': ')[1].strip('\n').split(' '))
        your_numbers_set = set(your_numbers.strip('').split(' '))
        overlap = winnning_numbers_set & your_numbers_set
        overlap.discard('')
        if len(overlap) > 0:
            score += 2**(len(overlap) - 1)

print(score)

# part 2
score2 = 0
copies_of_subsequent_cards = [1]
with open('2023/day4/input.txt') as file:
    for line in file.readlines():
        try:
            number_of_cards = copies_of_subsequent_cards.pop(0)
        except IndexError:
            number_of_cards = 1
        score2 += number_of_cards
        winnning_numbers, your_numbers = line.strip('\n').split(' | ')
        winnning_numbers_set = set(
            winnning_numbers.split(': ')[1].strip('\n').split(' '))
        your_numbers_set = set(your_numbers.strip('').split(' '))
        overlap = winnning_numbers_set & your_numbers_set
        overlap.discard('')
        for i in range(len(overlap)):
            try:
                copies_of_subsequent_cards[i] += number_of_cards
            except IndexError:
                copies_of_subsequent_cards.append(1 + number_of_cards)

print(score2)
