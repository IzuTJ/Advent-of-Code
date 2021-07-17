file = open("input.txt","r")
lines = file.readlines()

sector_id = [int(x[-11:-8]) for x in lines]
checksum = [x[-7:-2] for x in lines]

alphabets = [x[:-12] for x in lines]
sorted_alphabets = list()
result = []
sum_id = 0


def caesar(message: str, key: int):
	key %= 26
	answer = ""
	for char in message:
		num = ord(char)
		if num + key > 122:
			char_id = -122 + 96 + key + num
		else:
			char_id = key + num
		answer += chr(char_id)
	return answer

for i in range(len(alphabets)):
	count = dict()
	alphabets[i] = alphabets[i].replace("-","")
	
	# count the number of instances of alphabets, store them in a dictionary and sort the dictionary using lambda function
	for j in alphabets[i]:
		count[j] = count.get(j,0) + 1
	count = dict(sorted(count.items(), key= lambda x:x[1], reverse=True))
	
	# convert the items to a list to make it subscriptable
	count_list = list(count.items())
	
	x = 0
	sorted_alphabets.append("")
	while x<5 :
		if count_list[x][1] > count_list[x+1][1]:
			sorted_alphabets[i] += count_list[x][0]
		else: # complicated tiebreaker shit
			y = x
			temp = list()
			temp.append(count_list[y][0])
			while count_list[y][1] == count_list[y+1][1]:
				temp.append(count_list[y+1][0])
				y += 1
				if y>=len(count_list)-1:
					break
			temp.sort()
			for each in temp:
				sorted_alphabets[i] += each
				if len(sorted_alphabets[i]) == 5:
					break
			x = y	
		x += 1
	
	if checksum[i] == sorted_alphabets[i]:
		result.append((alphabets[i],sector_id[i]))
		sum_id += sector_id[i]

for each in result:
	print(caesar(each[0],each[1]),each[1])
