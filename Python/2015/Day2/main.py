file = open("input.txt", 'r')
present_string = file.read()
file.close()

# splits up the string twice to store dimensions of boxes as lists in a list of presents
# the dimensions will still be in string form, they will be converted just before calculation
present_list = present_string.split("\n")
for i in range(0, len(present_list)):
    present_list[i] = present_list[i].split('x')

total_area = 0

for box in present_list:
    # the three different rectangular areas are calculated here
    # the smallest of these is also stored separately to be added as extra
    a = int(box[0]) * int(box[1])
    b = int(box[1]) * int(box[2])
    c = int(box[2]) * int(box[0])
    extra_area = min(a, b, c)
    total_area += 2*a + 2*b + 2*c + extra_area

print(total_area)
