def get_forest_grid():
    forest_grid = []
    with open('2022/day8/input.txt') as file:
        for line in file.readlines():
            line = line.strip()
            forest_grid.append(list(line))
    return forest_grid


forest_grid = get_forest_grid()
visible_trees = 0

# Add all outer rim
visible_trees += len(forest_grid[0]) * 2  # upper and lower rim
visible_trees += len(forest_grid) * 2  # left and right edge
visible_trees -= 4  # subtract double counted corners

# loop through all remaining trees and check if they are the highest in the subset of the list
# form one of the sites
for x_coordinate in range(1, len(forest_grid) - 1):
    for y_coordinate in range(1, len(forest_grid[0]) - 1):
        tree_coordinates = (x_coordinate, y_coordinate)
        tree_height = forest_grid[x_coordinate][y_coordinate]

        view_from_left = forest_grid[x_coordinate][:y_coordinate]
        view_from_right = forest_grid[x_coordinate][y_coordinate + 1:]
        view_from_top = [
            forest_grid[x][y_coordinate] for x in range(x_coordinate)
        ]
        view_from_bottom = [
            forest_grid[x][y_coordinate]
            for x in range(x_coordinate + 1, len(forest_grid))
        ]
        if tree_height > max(view_from_left) or tree_height > max(
                view_from_bottom) or tree_height > max(
                    view_from_top) or tree_height > max(view_from_right):
            visible_trees += 1
        continue


#### For part two, the same forest grid can be used
forest_grid = get_forest_grid()

highest_view = 0
for x_coordinate in range(1, len(forest_grid)):  # everything in the grid can be disregarded
    for y_coordinate in range(1, len(forest_grid[x_coordinate])):  # This allows for not equal rows
        tree_height = forest_grid[x_coordinate][y_coordinate]
        left_view = right_view = upper_view = bottom_view = 0  # initiate parameters
        for tree_coordinate in range(x_coordinate + 1, len(forest_grid)):
            right_view += 1
            if forest_grid[tree_coordinate][y_coordinate] >= tree_height:
                break
        for tree_coordinate in range(x_coordinate - 1, -1, -1):
            left_view += 1
            if forest_grid[tree_coordinate][y_coordinate] >= tree_height:
                break
        for tree_coordinate in range(y_coordinate + 1, len(forest_grid)):
            upper_view += 1
            if forest_grid[x_coordinate][tree_coordinate] >= tree_height:
                break
        for tree_coordinate in range(y_coordinate - 1, -1, -1):
            bottom_view += 1
            if forest_grid[x_coordinate][tree_coordinate] >= tree_height:
                break

        highest_view = max(highest_view, left_view * right_view * bottom_view * upper_view)