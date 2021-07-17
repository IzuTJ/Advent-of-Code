file = open("input.txt","r")
lines = file.readlines()

count = 0
triangles = [x.split() for x in lines]
for i in range(len(triangles)):
	for j in range(3):
		triangles[i][j] = int(triangles[i][j])
	triangles[i].sort()
	if triangles[i][2]<(triangles[i][0]+triangles[i][1]):
		count += 1

print(count)