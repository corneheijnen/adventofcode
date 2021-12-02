import pandas as pd

depths = pd.read_csv('day1/input.txt', names=['depth'])
depths['diff'] = depths['depth'].diff()
depths['increase'] = depths['diff'] > 0

outcome = depths['increase'].sum()


# And now as one-liner
outcome = (pd.read_csv('day1/input.txt').diff() > 0).sum()


# Part 2
depths = pd.read_csv('day1/input.txt', names=['depth'])
depths['diff'] = depths['depth'].diff(periods=3)
depths['increase'] = depths['diff'] > 0

outcome = depths['increase'].sum()
