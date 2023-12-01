class BridgeConfiguration():

    def __init__(self, x_coordinate, y_coordinate, epochs=0):
        self.x_coordinate_head = x_coordinate
        self.y_coordinate_head = y_coordinate
        self.x_coordinate_tail = x_coordinate
        self.y_coordinate_tail = y_coordinate
        self.head_location = []
        self.tail_location = []

        self.epochs = epochs

    def __str__(self):
        print(
            f"Current head coordinates are: {self.x_coordinate_head}, {self.y_coordinate_head}"
        )
        print(
            f"Current tail coordinates are: {self.x_coordinate_tail}, {self.y_coordinate_tail}"
        )
        print(f"The amount of epochs run is: {self.epochs}")

    def update_position_head(self, direction):
        if direction == 'D':
            self.y_coordinate_head -= 1
        elif direction == 'U':
            self.y_coordinate_head += 1
        elif direction == 'R':
            self.x_coordinate_head += 1
        elif direction == 'L':
            self.x_coordinate_head -= 1

        self.head_location.append(
            (self.x_coordinate_head, self.y_coordinate_head))

    def update_position_tail(self):
        if self.x_coordinate_head - self.x_coordinate_tail > 1 and self.y_coordinate_head > self.y_coordinate_tail:
            self.x_coordinate_tail += 1
            self.y_coordinate_tail += 1
        elif self.x_coordinate_head - self.x_coordinate_tail > 1 and self.y_coordinate_head < self.y_coordinate_tail:
            self.x_coordinate_tail += 1
            self.y_coordinate_tail -= 1
        elif self.x_coordinate_head - self.x_coordinate_tail < -1 and self.y_coordinate_head > self.y_coordinate_tail:
            self.x_coordinate_tail -= 1
            self.y_coordinate_tail += 1
        elif self.x_coordinate_head - self.x_coordinate_tail < -1 and self.y_coordinate_head < self.y_coordinate_tail:
            self.x_coordinate_tail -= 1
            self.y_coordinate_tail -= 1
        elif self.y_coordinate_head - self.y_coordinate_tail > 1 and self.x_coordinate_head > self.x_coordinate_tail:
            self.x_coordinate_tail += 1
            self.y_coordinate_tail += 1
        elif self.y_coordinate_head - self.y_coordinate_tail > 1 and self.x_coordinate_head < self.x_coordinate_tail:
            self.x_coordinate_tail -= 1
            self.y_coordinate_tail += 1
        elif self.y_coordinate_head - self.y_coordinate_tail < -1 and self.x_coordinate_head > self.x_coordinate_tail:
            self.x_coordinate_tail += 1
            self.y_coordinate_tail -= 1
        elif self.y_coordinate_head - self.y_coordinate_tail < -1 and self.x_coordinate_head < self.x_coordinate_tail:
            self.x_coordinate_tail -= 1
            self.y_coordinate_tail -= 1

        elif self.x_coordinate_head - self.x_coordinate_tail > 1:
            self.x_coordinate_tail += 1  # move 1 to the right in case the diff is big
        elif self.x_coordinate_head - self.x_coordinate_tail < -1:
            self.x_coordinate_tail -= 1  # move 1 to the left
        elif self.y_coordinate_head - self.y_coordinate_tail > 1:
            self.y_coordinate_tail += 1  # move 1 upwards
        elif self.y_coordinate_head - self.y_coordinate_tail < -1:
            self.y_coordinate_tail -= 1  # Move 1 downwards
        self.tail_location.append((self.x_coordinate_tail, self.y_coordinate_tail))


    def get_unique_tail_locations(self):
        print(len(set(self.tail_location)))
        return set(self.tail_location)

test = BridgeConfiguration(0, 0)

with open('2022/day9/input.txt') as file:
    for line in file.readlines():
        direction, reps = line.strip().split(' ')
        for rep in range(int(reps)):
            print(direction, reps)
            test.update_position_head(direction)
            test.update_position_tail()

temp = test.get_unique_tail_locations()