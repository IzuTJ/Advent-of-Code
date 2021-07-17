import hashlib

file = open("input.txt", 'r')
key = file.read()
file.close()

addit = 0
count = 0
password = [0, 0, 0, 0, 0, 0, 0, 0]
while True:
	new_key = key + str(addit)
	hashed = hashlib.md5(new_key.encode()).hexdigest()
	if hashed[:5] == '00000':
		try:
			i = int(hashed[5])
			if password[i] == 0:
				password[i] = hashed[6]
				count += 1
		except:
			pass	
	if count == 8:
		break
	addit += 1
print(password)
