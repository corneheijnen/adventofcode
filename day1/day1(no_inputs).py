
# Read file
with open ('day1/input.txt') as file:
    depths = file.read().split('\n')[:-1] # to prevent last line from being wrong


# No inputs part 1
outcome = 0
for index in range(1, len(depths)):
    if int(depths[index]) - int(depths[index-1]) > 0:
        outcome += 1
print(outcome)


# No inputs part 2
outcome = 0
for index in range(3, len(depths)):
    if int(depths[index]) - int(depths[index-3]) > 0:
        outcome += 1
print(outcome)


# Oneliner with variable
periods = 3
print(len([depths[index] for index in range(periods, len(depths)) if int(depths[index]) - int(depths[index-3]) > 0]))