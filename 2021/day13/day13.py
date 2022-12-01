import numpy as np
dots = []
folds = []

with open('day13/input.txt') as file:
    for line in file.readlines():
        if len(line.split(',')) == 2:
            dots.append(line.strip().split(','))
        elif line[:4] == 'fold':
            folds.append(line.rstrip())


# Calculate dimensions of paper
xmax = max([int(coordinate[1]) for coordinate in dots])
ymax = max([int(coordinate[0]) for coordinate in dots])

# Create paper
paper = [[0] * (ymax + 1) for i in range(xmax + 1)]

# Create holes
for coordinates in dots:
    paper[int(coordinates[1])][int(coordinates[0])] = 1

# Make fold
for i in range(len(folds)):
    print(fold)
    fold = folds[i]

    new_paper = []

    if fold.split('=')[0][-1] == 'y':
        for x_coordinate in range(int(fold.split('=')[1])):
            new_row = []
            for y_coordinate in range(len(paper[0])):
                value = paper[x_coordinate][y_coordinate] + paper[len(paper) - x_coordinate - 1][y_coordinate]
                new_row.append(value)
            new_paper.append(new_row)
    else:
        for x_coordinate in range(len(paper)):
            new_row = []
            for y_coordinate in range(int(fold.split('=')[1])):
                value = paper[x_coordinate][y_coordinate] + paper[x_coordinate][len(paper[0]) - 1 - y_coordinate]
                new_row.append(value)
            new_paper.append(new_row)

    paper = new_paper

counter = 0
for row in new_paper:
    for value in row:
        if value > 0:
            counter += 1

for row in new_paper:
    row = ["#" if value > 0 else ' ' for value in row]
    print(''.join(row))