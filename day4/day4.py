import pandas as pd

counter = 0
cards_dict = {}
row = 1
cards_counter = 0
columns = ['column1', 'column2', 'column3', 'column4', 'column5']
cards_df = pd.DataFrame(columns=columns)
with open('day4/input.txt') as file:
    number_sequence = file.readline().split(',')
    for line in file.readlines():
        if line == '\n':
            continue
        line = line.replace('  ', ' ')
        temp = line.strip().split(' ')
        print(temp)
        cards_df = cards_df.append(dict(zip(columns, temp)), ignore_index=True)
        if row == 5:
            cards_dict[cards_counter] = cards_df
            cards_df = pd.DataFrame()
            cards_counter += 1
            row = 0
        row += 1

def get_outcome(number_sequence, cards_dict):
    for number in number_sequence:
        print(number)
        print(f"Checking {number} in all bingo cards")

        for key, values in cards_dict.items():
            cards_dict[key] = values.replace(str(number), -1)
            if (cards_dict[key].sum() == - 5).any() or (cards_dict[key].sum(axis=1) == - 5).any():
                print(number)
                print(cards_dict[key])
                return cards_dict[key], number


frame, number = get_outcome(number_sequence, cards_dict)
sum = frame.replace(-1, 0)
for column in sum.columns:
    sum[column] = sum[column].astype(int)

answer = sum.sum().sum() * int(number)