from collections import Counter

# Part 1
mapping='23456789TJQKA'

first, second, third, fourth, fifth, sixth, seventh = ({} for i in range(7))
with open('2023/day7/input.txt') as file:
    for line in file.readlines():
        cards_string, bid = line.strip().split(' ')
        cards_counter = Counter(cards_string)
        if cards_counter.most_common(1)[0][1] == 5:
            first[cards_string] = bid
        elif cards_counter.most_common(1)[0][1] == 4:
            second[cards_string] = bid
        elif cards_counter.most_common(1)[0][1] == 3:
            if cards_counter.most_common(2)[1][1] == 2:
                third[cards_string] = bid
            else:
                fourth[cards_string] = bid
        elif cards_counter.most_common(1)[0][1] == 2:
            if cards_counter.most_common(2)[1][1] == 2:
                fifth[cards_string] = bid
            else:
                sixth[cards_string] = bid
        else:
            seventh[cards_string] = bid

total_sum = 0
counter = 0
for dictionary in [seventh, sixth, fifth, fourth, third, second, first]:
    sorted_keys = sorted(dictionary.keys(), key=lambda hand: [mapping.index(c) for c in hand])
    for key in sorted_keys:
        counter += 1
        total_sum += int(dictionary[key]) * counter

print(total_sum)

# part 2
mapping='J23456789TQKA'

first, second, third, fourth, fifth, sixth, seventh = ({} for i in range(7))
with open('2023/day7/input.txt') as file:
    for line in file.readlines():
        cards_string, bid = line.strip().split(' ')
        jokers = cards_string.count('J')
        if jokers == 5:
            first[cards_string] = bid
        else:
            cards_counter = Counter(cards_string)
            try:
                cards_counter.pop('J')
            except KeyError:
                pass
            if cards_counter.most_common(1)[0][1] + jokers == 5:
                first[cards_string] = bid
            elif cards_counter.most_common(1)[0][1] + jokers == 4:
                second[cards_string] = bid
            elif cards_counter.most_common(1)[0][1] + jokers == 3:
                if cards_counter.most_common(2)[1][1] == 2:
                    third[cards_string] = bid
                else:
                    fourth[cards_string] = bid
            elif cards_counter.most_common(1)[0][1] + jokers == 2:
                if cards_counter.most_common(2)[1][1] == 2:
                    fifth[cards_string] = bid
                else:
                    sixth[cards_string] = bid
            else:
                seventh[cards_string] = bid

total_sum = 0
counter = 0
for dictionary in [seventh, sixth, fifth, fourth, third, second, first]:
    sorted_keys = sorted(dictionary.keys(), key=lambda hand: [mapping.index(c) for c in hand])
    for key in sorted_keys:
        counter += 1
        total_sum += int(dictionary[key]) * counter

print(total_sum)