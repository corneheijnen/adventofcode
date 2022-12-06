with open('2022/day6/input.txt') as file:
    text = str(file.readlines()[0])
    for i in range(len(text) - 5):
        print(text[i:i+14])
        if len(set(text[i:i+14])) == 14:
            print(i + 14)
            print(text[i:i+14])
            break