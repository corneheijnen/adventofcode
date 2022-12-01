import pandas as pd

# read input
movements = pd.read_csv('day2/input.txt', names=['direction', 'size'], sep=' ')

# groupby by direction to find locations
totals = movements.groupby('direction').sum()

# get movements
horizontal = totals.loc['forward']['size']
depth = totals.loc['down']['size'] - totals.loc['up']['size']

# Calculate outcome
outcome = horizontal * depth
print(outcome)


# Part 2

# determine horizontal cumulative sum
movements['horizontal'] = movements.loc[movements['direction'] == 'forward', 'size'].cumsum()

# Determine aim at each point
movements.loc[movements['direction'] == 'down', 'aim'] = movements['size']
movements.loc[movements['direction'] == 'up', 'aim'] = - movements['size']
movements.loc[movements['direction'] == 'forward', 'aim'] = 0
movements['aim'] = movements['aim'].fillna(0).cumsum()

# Calculate cumulative depth
movements['depth'] = 0
movements.loc[movements['direction'] == 'forward', 'depth'] = movements['size'] * movements['aim']
depth2 = movements['depth'].sum()

product2 = horizontal * depth2
print(product2)