file = open("input.txt", "r")
coded = file.read().split()

for j in range(8):
	count = dict()
	for i in coded:
			count[i[j]] = count.get(i[j],0) + 1
	
	count = dict(sorted(count.items(), key= lambda x:x[1], reverse=True))
	print(list(count.items())[0])
	print(list(count.items())[-1])