output_dict = {}
with open('2023/day6/input.txt') as file:
    for line in file.readlines():
        type, values = line.strip().split(': ')
        # values = [value for value in values.split(' ') if len(value) > 0]
        values = values.strip().replace(' ', '')
        output_dict[type] = [values]

calculation_score = 1
for i in range(len(output_dict['Time'])):
    value = 0
    time = int(output_dict['Time'][i])
    distance_record = int(output_dict['Distance'][i])
    for power_down_time in range(0, time + 1):
        distance = (time - power_down_time) * power_down_time
        if distance > distance_record:
            # print(power_down_time, distance, distance_record)
            value += 1
    calculation_score *= value

print(calculation_score)


