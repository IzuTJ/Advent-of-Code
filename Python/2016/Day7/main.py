file = open("input.txt", "r")
addresslist = file.read().split()
TSL_IPs = list()
SSL_IPs = list()


def find_abba(target:str):
	for i in range(len(target)-3):
		if target[i]==target[i+3] and target[i]!=target[i+1] and target[i+1]==target[i+2]:
			return True
	return False


def find_aba(target:str):
	aba = []
	for i in range(len(target)-2):
		if target[i]==target[i+2] and target[i]!=target[i+1]:
			aba.append(target[i:i+3])
	return aba


# run through the whole list of IP  addresses, split them into strings separated by []
for i in range(len(addresslist)):	
	addresslist[i] = addresslist[i].replace("[", "]")
	addresslist[i] = addresslist[i].split("]")

	# run throught the different parts of each IP to find abba
	j = 1
	while True:
		odd = find_abba(addresslist[i][j])
		j+=2
		if odd or j>=len(addresslist[i]):
			break

	if not odd:
		j = 0
		while True:
			even = find_abba(addresslist[i][j])
			j+=2
			if even:
				TSL_IPs.append(addresslist[i])
				break
			if j>=len(addresslist[i]):
				break
	
	# find all the aba and bab
	
	aba_list = list()
	bab_list = list()

	for j in range(len(addresslist[i])):
		if j%2==0:
			aba_list += find_aba(addresslist[i][j])
		else:
			bab_list += find_aba(addresslist[i][j])
	for aba in aba_list:
		bab = aba[1]+aba[0]+aba[1]
		if bab in bab_list:
			SSL_IPs.append(addresslist[i])
			break

print(len(TSL_IPs), len(SSL_IPs))