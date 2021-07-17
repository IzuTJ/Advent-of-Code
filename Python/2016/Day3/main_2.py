file = open("input.txt","r")
numbers = file.read().split()

count = 0
list1 = []
list2 = []
list3 = []

for i in range(len(numbers)):
	if i%3 == 0:
		list1.append(int(numbers[i]))
	elif i%3 == 1:
		list2.append(int(numbers[i]))
	elif i%3 ==2:
		list3.append(int(numbers[i]))

sorted_numbers = list1 + list2 + list3
triangles = []

for i in range(len(sorted_numbers)//3):
	triangles.append([sorted_numbers[i*3],sorted_numbers[i*3+1],sorted_numbers[i*3+2]])
	triangles[i].sort()
	if triangles[i][2]<(triangles[i][0]+triangles[i][1]):
		count += 1

print(count)