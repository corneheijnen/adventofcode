import pandas as pd

playing_field = pd.read_csv('day9/input.txt', names=['string'], dtype='str')
playing_field = playing_field['string'].str.split('', expand=True).replace('', 99)
playing_field.loc[playing_field.shape[0]] = len(playing_field.columns) * [99]
playing_field.loc[-1] = len(playing_field.columns) * [99]
playing_field = playing_field.astype(int)
playing_field.sort_index(inplace=True)
playing_field.reset_index(drop=True, inplace=True)

def is_mininum(df, row, column):
    """:param"""

    original_value = df.at[row, column]

    if (original_value < df.at[row -1, column] and original_value < df.at[row + column]
            and original_value < df.at[row, column - 1] and original_value < df.at[row + column + 1]):
        return True
    else:
        return False

result = 0
minimums = []
for row in range(1, playing_field.shape[0] -1):
    for column in range(1, len(playing_field.columns) -1):
        depth = playing_field.at[row, column]
        if depth < playing_field.at[row - 1, column] and depth < playing_field.at[row + 1, column] and depth < playing_field.at[row, column - 1] and depth < playing_field.at[row, column + 1]:
            minimums.append([row, column])
            result = result + depth + 1

# Part 2
# playing_field = pd.read_csv('day9/input.txt', names=['string'], dtype='str')
# playing_field = playing_field['string'].str.split('', expand=True).drop(columns=[0, 101])
# playing_field = playing_field.astype(int)
# playing_field.sort_index(inplace=True)
# playing_field.reset_index(drop=True, inplace=True)

# Create bassins
playing_field = playing_field > 8

def calculate_bassins(playing_field, minimums):
    """Determine size of bassins"""

    output = {}

    # Loop through all low points
    for low_point in minimums:
        # Initiate a set of points belonging to this bassin
        bassin = set()
        # Add starting point to the set
        bassin.add(tuple(low_point))
        # Retrieve all current points
        current_points = [low_point]

        growth_in_epoch = True

        while growth_in_epoch:
            # Save size of bassin
            start_size = len(bassin)

            # Retrieve all neighbours of current points
            to_investigate = set()
            for point in current_points:
                neighbours = retrieve_neighbours(point)
                to_investigate.update(tuple(neighbours))
            # Check all neighbours

            new_points = []
            for neighbour in to_investigate:
                # Add if neighbour is not height 9
                try:
                    if not playing_field.at[neighbour[0], neighbour[1]]:
                        bassin.add(tuple(neighbour))
                        new_points.append(neighbour)
                except KeyError:
                    continue

            current_points = new_points
            if len(bassin) == start_size:
                growth_in_epoch = False
                output[tuple(low_point)] = len(bassin)

    return output

def retrieve_neighbours(low_point):
    neighbours = []
    neighbours.append((low_point[0], low_point[1] - 1))
    neighbours.append((low_point[0], low_point[1] + 1))
    neighbours.append((low_point[0] - 1, low_point[1]))
    neighbours.append((low_point[0] + 1, low_point[1]))

    return neighbours


output = calculate_bassins(playing_field, minimums)
sizes = sorted(output.values())

print(sizes[-3] * sizes[-2] * sizes[-1])