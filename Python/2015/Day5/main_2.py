file = open("input.txt", 'r')
string_list = file.read().split()
file.close()

nice_string_list = []
for string in string_list:
	double = False
	has_pair = False
	pair_list = []

	for i in range(len(string)):
		try:
			pair_list.append(string[i]+string[i+1])
			if string[i] == string[i+2]:
				double = True
		except:
			pass
	match_list = []
	for j in range(len(pair_list)):
		for k in range(j,len(pair_list)):
			if pair_list[k] == pair_list[j] and abs(k-j)>=2:
				has_pair = True
				break

	if double and has_pair:
		nice_string_list.append(string)
print(len(nice_string_list))