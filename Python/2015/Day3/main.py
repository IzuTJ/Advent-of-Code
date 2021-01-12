file = open("input.txt", 'r')
direction_data = file.read()
file.close()

direction_domain = ('^', '>', 'v', '<')


class Coordinates:
    def __init__(self):
        self.x = 0
        self.y = 0


def coordinate_change(direction, coordinates):

    # code for changing the co-ordinates based on direction and magnitude
    if direction == '^':
        coordinates.y += 1

    elif direction == '>':
        coordinates.x += 1

    elif direction == 'v':
        coordinates.y -= 1

    elif direction == '<':
        coordinates.x -= 1

    return coordinates


# Initial conditions
santa = Coordinates()
robo_santa = Coordinates()
all_visited_coordinates = [str(santa.x) + '|' + str(santa.y)]

for i, step in enumerate(direction_data):
    if (i % 2) == 0:
        santa = coordinate_change(step, santa)
        all_visited_coordinates.append(str(santa.x) + '|' + str(santa.y))
    else:
        robo_santa = coordinate_change(step, robo_santa)
        all_visited_coordinates.append(str(robo_santa.x) + '|' + str(robo_santa.y))

print(all_visited_coordinates)
print(len(set(all_visited_coordinates)))
