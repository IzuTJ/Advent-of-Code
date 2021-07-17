file = open("input.txt", 'r')
string_list = file.read().split()
file.close()

nice_string_list = []
for string in string_list:
	vowel_count = 0
	double = False
	cons = True

	for i in range(len(string)):
		try:
			if string[i:i+2] in ["ab","cd","pq","xy"]:
				cons = False
			if string[i] == string[i+1]:
				double = True
		except:
			pass

		if string[i] in ['a','e','i','o','u']:
			vowel_count += 1
	
	if vowel_count>=3 and double and cons:
		nice_string_list.append(string)

print(len(nice_string_list))