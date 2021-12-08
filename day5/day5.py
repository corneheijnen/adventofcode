import pandas as pd

functions = pd.read_csv('day5/input.txt', names=['y1', 'x1', 'y2', 'x2'], sep=' -> |,')

field = pd.DataFrame(0, index=range(1000), columns=range(1000))
# field = pd.DataFrame(0, index=range(10), columns=range(10))



for index in range(functions.shape[0]):
    continue_loop = True
    not_diagonal = True
    coordinates = []
    test_one = functions.iloc[index]
    while continue_loop:
        if test_one['x1'] != test_one['x2'] and test_one['y1'] != test_one['y2']:
            # not_diagonal = False
            field.at[test_one['x1'], test_one['y1']] += 1

            if test_one['x1'] - test_one['x2'] > 0:
                test_one['x1'] -= 1
            else:
                test_one['x1'] += 1

            if test_one['y1'] - test_one['y2'] > 0:
                test_one['y1'] -= 1
            else:
                test_one['y1'] += 1


        elif test_one['x1'] != test_one['x2']:
            field.at[test_one['x1'], test_one['y1']] += 1
            if test_one['x1'] - test_one['x2'] > 0:
                test_one['x1'] -= 1
            else:
                test_one['x1'] += 1

        elif test_one['y1'] != test_one['y2']:
            field.at[test_one['x1'], test_one['y1']] += 1
            if test_one['y1'] - test_one['y2'] > 0:
                test_one['y1'] -= 1
            else:
                test_one['y1'] += 1

        else:
            if not_diagonal:
                field.at[test_one['x1'], test_one['y1']] += 1
            continue_loop = False

answer = (field > 1).sum().sum()
