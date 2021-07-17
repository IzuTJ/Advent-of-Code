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
			j += 1
			if j>2: j = 2
		elif each == 'L':
			j -=1
			if j<0: j = 0
		elif each == 'U':
			i -=1
			if i<0: i = 0
		elif each == 'D':
			i += 1
			if i>2: i = 2

	code += str(keypad[i][j])

print(code)
