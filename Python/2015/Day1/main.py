file = open("input.txt", "r")
char_input = file.read()
floor_counter = 0

for char in char_input:
    if char == '(':
        floor_counter += 1
    if char == ')':
        floor_counter -= 1

print(floor_counter)
