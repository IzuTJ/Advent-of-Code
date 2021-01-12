import hashlib

file = open("input.txt", 'r')
key = file.read()
file.close()

addit = 1
flag = True

while flag:
    new_key = key + str(addit)
    result = hashlib.md5(new_key.encode())
    x = str(result.hexdigest())
    if x[:6] == '000000':
        flag = False
        break
    addit += 1

print(addit)
