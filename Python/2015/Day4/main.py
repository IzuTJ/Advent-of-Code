import hashlib

file = open("input.txt", 'r')
key = file.read()
file.close()

addit = 1

while True:
    new_key = key + str(addit)
    result = hashlib.md5(new_key.encode())
    x = str(result.hexdigest())
    if x[:6] == '000000':
        break
    addit += 1

print(addit)
