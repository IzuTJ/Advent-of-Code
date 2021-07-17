import hashlib

file = open("input.txt", 'r')
key = file.read()
file.close()

addit = 0
password = ""
while True:
	new_key = key + str(addit)
	hashed = hashlib.md5(new_key.encode())
	x = str(hashed.hexdigest())
	if x[:5] == '00000':
		password += x[5]
	if len(password) == 8:
		break
	addit += 1
print(password)
