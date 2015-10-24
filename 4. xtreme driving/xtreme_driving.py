from __future__ import print_function

units_cows = raw_input()

units, number_of_cows = units_cows.split(" ")

units = int(units)
number_of_cows = int(number_of_cows)

# print("units: ", units)
# print("number_of_cows: ", number_of_cows)

cows = []
for _ in range(number_of_cows):
    coordinates = raw_input()
    coordinates = coordinates.split(" ")
    cow_lane = int(coordinates[0])
    cow_unit = int(coordinates[1])

    cows.append( (cow_lane, cow_unit) )


# print(cows)

def number_of_paths(position):
    """
    TODO
    add heuristic for blocked road
    """
    if position in cows:
        return 0

    if position[0] < 1:
        return 0

    if position[0] > 4:
        return 0

    if position[1] == units:
        if position[0] == 1:
            return 1
        else:
            return 0

    num_paths = 0

    num_paths += number_of_paths( (position[0], position[1] + 1) )

    num_paths += number_of_paths( (position[0] - 1, position[1] + 1) )

    num_paths += number_of_paths( (position[0] + 1, position[1] + 1) )

    return num_paths


position = (1, 1)

num_paths = number_of_paths(position)

print(num_paths % (10**9 + 7))
