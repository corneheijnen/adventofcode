import pandas as pd

playing_field = pd.read_csv('day9/input.txt', names=['string'], dtype='str')
playing_field = playing_field['string'].str.split('', expand=True).replace('', 99)
playing_field.loc[playing_field.shape[0]] = len(playing_field.columns) * [99]
playing_field.loc[-1] = len(playing_field.columns) * [99]
playing_field = playing_field.astype(int)
playing_field.sort_index(inplace=True)
playing_field.reset_index(drop=True, inplace=True)

def is_mininum(df, row, column):
    """:param"""

    original_value = df.at[row, column]

    if (original_value < df.at[row -1, column] and original_value < df.at[row + column]
            and original_value < df.at[row, column - 1] and original_value < df.at[row + column + 1]):
        return True
    else:
        return False

result = 0
for row in range(1, playing_field.shape[0] -1):
    for column in range(1, len(playing_field.columns) -1):
        depth = playing_field.at[row, column]
        if depth < playing_field.at[row - 1, column] and depth < playing_field.at[row + 1, column] and depth < playing_field.at[row, column - 1] and depth < playing_field.at[row, column + 1]:
            print(depth)
            result = result + depth + 1


# Part 2
