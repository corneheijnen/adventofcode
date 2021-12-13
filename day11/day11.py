from typing import List

with open ('day11/input_simple.txt') as file:
    data = [list(row[:-1]) for row in file.readlines()]

class OctopusGrid():
    """The octopus grid"""

    def __init__(self, grid: List[List]):
        self.grid = grid
        self.flashes = 0
        self.to_reset = [len(self.grid) * [False]] * len(self.grid[0])

    def next_step(self):
        """Let one step pass"""

        # part 1: increase energy for each octopus by one
        for index1, row in enumerate(self.grid):
            for index2, value in enumerate(row):
                self.grid[index1][index2] = int(self.grid[index1][index2]) + 1

        # part 2: Create flashes
        while sum([sum(value > 9 for value in row) for row in self.grid]) > sum([sum(value for value in row) for row in self.to_reset]):
            self.flashes += sum([sum(value > 9 for value in row) for row in self.grid])
            for index1, row in enumerate(self.grid):
                for index2, value in enumerate(row):
                    if self.grid[index1][index2] > 9 and self.to_reset[index1][index2] == False:
                        self.to_reset[index1][index2] = True
                        self.grid[index1][index2] -=1
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                try:
                                    self.grid[index1 - i][index2 - j] += 1
                                except IndexError:
                                    continue

        print(self.to_reset)
        # part 3: reset high values and self.to_reset
        for index1, row in enumerate(self.to_reset):
            for index2, value in enumerate(row):
                if self.to_reset[index1][index2]:
                    self.grid[index1][index2] = 0

        self.to_reset = [len(self.grid) * [False]] * len(self.grid[0])

grid = OctopusGrid(data)
for i in range(5):
    print (60 * '#')
    for row in grid.grid:
        print(row)
    grid.next_step()
    print(60 * '#')

with open ('day11/input_simple.txt') as file:
    data = [list(row[:-1]) for row in file.readlines()]

class OctopusGrid():
    """The octopus grid"""

    def __init__(self, grid: List[List]):
        self.grid = grid
        self.flashes = 0
        self.to_reset = [len(self.grid) * [False]] * len(self.grid[0])

    def next_step(self):
        """Let one step pass"""

        # part 1: increase energy for each octopus by one
        for index1, row in enumerate(self.grid):
            for index2, value in enumerate(row):
                self.grid[index1][index2] = int(self.grid[index1][index2]) + 1

        # part 2: Create flashes
        while sum([sum(value > 9 for value in row) for row in self.grid]) > sum([sum(value for value in row) for row in self.to_reset]):
            self.flashes += sum([sum(value > 9 for value in row) for row in self.grid])
            for index1, row in enumerate(self.grid):
                for index2, value in enumerate(row):
                    if self.grid[index1][index2] > 9:
                        self.to_reset[index1][index2] = True
                        self.grid[index1][index2] -=1
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                try:
                                    self.grid[index1 - i][index2 - j] += 1
                                except IndexError:
                                    continue

        print(self.to_reset)
        # part 3: reset high values and self.to_reset
        for index1, row in enumerate(self.to_reset):
            for index2, value in enumerate(row):
                if self.to_reset[index1][index2]:
                    self.grid[index1][index2] = 0

        self.to_reset = [len(self.grid) * [False]] * len(self.grid[0])

grid = OctopusGrid(data)
for i in range(5):
    print (60 * '#')
    for row in grid.grid:
        print(row)
    grid.next_step()
    print(60 * '#')