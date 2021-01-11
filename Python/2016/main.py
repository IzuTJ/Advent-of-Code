file = open("input.txt", 'r')
direction_data = file.read()
file.close()
direction_data = direction_data.split(", ")

direction_domain = ('N', 'E', 'S', 'W')


class Coordinates:
    def __init__(self):
        self.x = 0
        self.y = 0


# Initial conditions
direction = 'N'
coordinates = Coordinates()
all_visited_coordinates = []


def direction_change(current_direction, change):
    # code for handling direction changes through L and R turns
    vector = direction_domain.index(current_direction)
    if change == 'R':
        if vector == 3:
            vector = -1
        vector += 1
    elif change == 'L':
        if vector == 0:
            vector = 4
        vector -= 1
    return direction_domain[vector]


def coordinate_change(current_direction, magnitude, current_coordinates):

    # code for changing the co-ordinates based on direction and magnitude
    if current_direction == 'N':
        current_coordinates.y += magnitude

    elif current_direction == 'E':
        current_coordinates.x += magnitude

    elif current_direction == 'S':
        current_coordinates.y -= magnitude

    elif current_direction == 'W':
        current_coordinates.x -= magnitude

    return current_coordinates


for step in direction_data:
    turn = step[0]
    mag = int(step[1:])

    direction = direction_change(direction, turn)
    coordinates = coordinate_change(direction, mag, coordinates)


print(coordinates.x, coordinates.y)
print("Total:" + str(abs(coordinates.x) + abs(coordinates.y)))
