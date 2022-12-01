
# Grab data
with open('day7/input.txt') as file:
    data = [int(i) for i in file.readline().split(',')]

best = 99999999999999999
position_result = -1
for position in range(1000):
    total_distance = sum([abs(position - i) * 0.5 * (abs(position - i) + 1) for i in data])
    if total_distance < best:
        best = total_distance
        position_result = position

print(best, position_result)

# Oneliner
print(int(min([sum([abs(j - i) * 0.5 * (abs(j - i) + 1) for i in [int(k) for k in open('day7/input.txt').readline().split(',')]]) for j in range(max([int(i) for i in open('day7/input.txt').readline().split(',')]))])))

