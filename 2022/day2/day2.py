points_dict = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

points = 0
with open('2022/day2/input.txt') as file:
    for line in file.readlines():
        points += points_dict[line[0:3]]

print(points)

points_dict2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}

points = 0
with open('2022/day2/input.txt') as file:
    for line in file.readlines():
        points += points_dict2[line[0:3]]

print(points)