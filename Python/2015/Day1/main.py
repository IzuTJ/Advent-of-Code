file = open("input.txt", "r")
char_input = file.read()
file.close()
floor_counter = 0
crossing_point = 0

for char in char_input:

    # counts which floor Santa is on right now
    if char == '(':
        floor_counter += 1
    if char == ')':
        floor_counter -= 1

    crossing_point += 1
    if floor_counter == -1:
        # print whenever you are at the first floor of the basement
        # disregards whether you came from above or below
        print(crossing_point)

print(floor_counter)
