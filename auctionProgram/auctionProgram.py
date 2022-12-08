auction_dict = {}
print("--> Welcome to the secret auction program. <--")
item = input("Provide the item to be auctioned: \n")
print("Add participants to an auction with their name and bid.")

def addParticipant(name, bid):
	auction_dict[name] = bid
	
def calculateWinner():
	max_bid = 0
	winner = ""
	for name, bid in auction_dict.items():
		if bid > max_bid:
			max_bid = bid
			winner = name
	print("The winner is {}. They got {} for ${}!!!!!!".format(winner, item, max_bid))

def auctionProgram():	
	name = input("Please provide the name: \n")
	bid = int(input("Please provide the bid: \n$"))
	addParticipant(name, bid)
	reply = input("Is there another participant? \n")
	if reply == "no":
		calculateWinner()
	else:
		auctionProgram()	
	
if __name__ == "__main__":
	auctionProgram()
