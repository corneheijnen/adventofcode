from typing import List

with open ('day11/input.txt') as file:
    data = [list(row[:-1]) for row in file.readlines()]

class OctopusGrid():
    """The octopus grid"""

    def __init__(self, grid: List[List]):
        self.grid = grid
        self.flashes = 0
        self.to_reset = [len(self.grid) * [False] for i in range(len(self.grid[0]))]

    def next_step(self):
        """Let one step pass"""


        # part 1: increase energy for each octopus by one
        for index1, row in enumerate(self.grid):
            for index2, value in enumerate(row):
                self.grid[index1][index2] = int(self.grid[index1][index2]) + 1

        # part 2: Create flashes
        while sum([sum(value > 9 for value in row) for row in self.grid]) > sum([sum(value for value in row) for row in self.to_reset]):

            # # print value
            # print('round of upgrading')
            # for row in self.grid:
            #     print(row)
            # print(60 * "#")

            for index1, row in enumerate(self.grid):
                for index2, value2 in enumerate(row):
                    if value2 > 9 and self.to_reset[index1][index2] == False:
                        self.to_reset[index1][index2] = True
                        for left in range(-1, 2):
                            for up in range(-1, 2):
                                if left == 0 and up == 0:
                                    pass
                                else:
                                    try:
                                        if index1 - left > -1 and index2 - up > - 1:
                                            self.grid[index1 - left][index2 - up] += 1
                                    except IndexError:
                                        pass
                    else:
                        pass

        self.flashes += sum([sum(value > 9 for value in row) for row in self.grid])

        # part 3: reset high values and self.to_reset
        for index1, row in enumerate(self.to_reset):
            for index2, value in enumerate(row):
                if self.to_reset[index1][index2]:
                    self.grid[index1][index2] = 0

        self.to_reset = [len(self.grid) * [False] for i in range(len(self.grid[0]))]

flashes_dict = {}
grid = OctopusGrid(data)
for i in range(1001):
    print(f"Iteration {i}: {grid.flashes}")
    grid.next_step()
    flashes_dict[i] = grid.flashes

    if i > 0 and flashes_dict[i] - flashes_dict[i - 1] == 100:
        print(f"100 flahes in one iteration: Answer is iteration {i + 1}")
        break
