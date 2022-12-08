from symbols import *

print("--> Welcome to ceasar's cipher <--")

def encode(message, shift):
	for i, symbol in enumerate(message):
		if symbol in letters_upper:
			message[i] = getNext(symbol, shift, True)	
		elif symbol in letters_lower:
			message[i] = getNext(symbol, shift)	
	print("Here is the encoded result: {}".format("".join(message)))
	
def decode(message, shift):
	for i, symbol in enumerate(message):
		if symbol in letters_upper:
			message[i] = getPrev(symbol, shift, True)	
		elif symbol in letters_lower:
			message[i] = getPrev(symbol, shift)	
	print("Here is the decoded result: {}".format("".join(message)))

def getNext(letter, shift, capital = False):
	if capital:
		idx = letters_upper.index(letter)
		if idx + shift > 25:
			return letters_upper[idx + shift - 26]
		else:
			return letters_upper[idx + shift]
	else:
		idx = letters_lower.index(letter)
		if idx + shift > 25:
			return letters_lower[idx + shift - 26]
		else:
			return letters_lower[idx + shift]
	
def getPrev(letter, shift, capital = False):
	if capital:
		idx = letters_upper.index(letter)
		if idx - shift < 0:
			return letters_upper[idx - shift + 26]
		else:
			return letters_upper[idx - shift]
	else:
		idx = letters_lower.index(letter)
		if idx - shift < 0:
			return letters_lower[idx - shift + 26]
		else:
			return letters_lower[idx - shift]
	
def ceasarCipher():
	cmd = input("Type \"encode\" to encrypt, \"decode\" to decrypt: \n")
	while cmd != "encode" and cmd != "decode":
		cmd = input("This is not a valid command. Type \"encode\" to encrypt, \"decode\" to decrypt: \n")
	msg = input("Type your message: \n")
	shift = input("Type the shift number: \n")
	while not shift.isdigit():
		shift = input("This is not valid. Please type an integer number: \n")
	shift = int(shift)
	if cmd == "encode":
		proc_msg = encode(list(msg), shift)
	else:
		proc_msg = decode(list(msg), shift)
	reply = input("Type \"yes\" if you want to continue. Otheriwse, type \"no\". \n")
	while reply != "yes" and reply != "no":
		reply = input("This is a not a valid reply. Type \"yes\" if you want to continue. Otheriwse, type \"no\". \n")
	if reply == "yes":
		print(" --------------------------- ")
		ceasarCipher()
	

if __name__ == "__main__":
	ceasarCipher()
