file = open("input.txt", "r")
instructions = file.readlines()

keypad = (
	(0, 0,  0,   0,   0, 0, 0),
	(0, 0,  0,   1,   0, 0, 0),
	(0, 0,  2,   3,   4, 0, 0),
	(0, 5,  6,   7,   8, 9, 0),
	(0, 0, 'A', 'B', 'C', 0, 0),
	(0, 0,  0,  'D',  0, 0, 0),
	(0, 0,  0,   0,   0, 0, 0))

code = ""

i = 3
j = 1 #starting indices at the center of the keypad

for line in instructions:
	for each in line:
		if each == 'R':
			if keypad[i][j+1] != 0:
				j += 1
		elif each == 'L':
			if keypad[i][j-1] != 0:
				j -=1
		elif each == 'U':
			if keypad[i-1][j] != 0:
				i -=1
		elif each == 'D':
			if keypad[i+1][j] != 0:
				i += 1

	code += str(keypad[i][j])

print(code)
