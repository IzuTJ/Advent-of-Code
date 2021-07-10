file = open("input.txt", 'r')
present_list = file.readlines()
file.close()

# splits up the string twice to store dimensions of boxes as lists in a list of presents
# the dimensions in string form are converted to integers

for i in range(0, len(present_list)):
    present_list[i] = present_list[i].split('x')
    for j in range(0, len(present_list[i])):
        present_list[i][j] = int(present_list[i][j])

total_area = 0

for box in present_list:
    # the three different rectangular areas are calculated here
    # the smallest of these is also stored separately to be added as extra
    a = box[0] * box[1]
    b = box[1] * box[2]
    c = box[2] * box[0]
    extra_area = min(a, b, c)
    total_area += 2 * a + 2 * b + 2 * c + extra_area

print(total_area)

total_length = 0

for box in present_list:
    # the three different rectangular perimeters are calculated here
    # the smallest of these is used and extra length is just the volume of the box
    a = box[0] + box[1]
    b = box[1] + box[2]
    c = box[2] + box[0]
    extra_length = box[0] * box[1] * box[2]
    total_length += min(a, b, c) * 2 + extra_length

print(total_length)
