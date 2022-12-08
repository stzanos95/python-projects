import random
import symbols

print("--> Welcome to the PyPassword Generator! <--")
lets = int(input("How many letters would you like in your password?\n"))
symbs = int(input("How many symbols would you like?\n"))
nums = int(input("How many numbers would you like?\n"))

sum_list = [lets, symbs, nums]
rpassword = ""

category = random.randint(0, 2)
for x in range(1, lets + symbs + nums + 1):
	while(sum_list[category] == 0):
		category = random.randint(0, 2)
	if category == 0:
		rpassword += symbols.letters[random.randint(0, len(symbols.letters)-1)]
	elif category == 1:
		rpassword += symbols.symbols[random.randint(0, len(symbols.symbols)-1)]
	else:
		rpassword += symbols.numbers[random.randint(0, len(symbols.numbers)-1)]
	sum_list[category] -= 1

print("Your randomly generated password: {}".format(rpassword))
		
	
		
