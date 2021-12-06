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
