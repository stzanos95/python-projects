import random
import time

print("--> BLACK JACK <--")

def newDeck():
	deck = []
	for num in range(2, 11):
		deck += [str(num)]*4
	for figure in "JQKA":
		deck += [figure]*4
	return deck
	
def drawCard(hand, deck):
	card = deck.pop(random.randint(0, len(deck)-1))
	hand.append(card)
	return hand, deck
	
def startingPhase(playerHand, dealerHand, deck):
	for i in range(0, 2):
		playerHand, deck = drawCard(playerHand, deck)
		dealerHand, deck = drawCard(dealerHand, deck)
	return playerHand, dealerHand, deck

def showHand(hand, score, isDealer=False, isFirstDeal=False):
	if isDealer:
		if isFirstDeal:
			print("Dealer hand: {}, ??".format(hand[0]))
		else:
			print("Dealer hand: {} \nScore: {}".format(", ".join(hand), score))
	else:
		print("Player hand: {} \nScore: {}".format(", ".join(hand), score))
	
	
def calculateHand(hand):	
	if hand == ["A", "A"]:
		hasLost = False
		isBlackJack = True
		score = 21
	else:
		isBlackJack = False
		score = 0
		firstAce = True
		for card in hand:
			if card in "JQK":
				score += 10
			elif card == "A":
				if firstAce:
					if score + 11 > 21:
						score += 1
					else:
						score += 11
					firstAce = False
				else:
					score += 1
			else:
				score += int(card)
		if score > 21:
			hasLost = True
		else:
			hasLost = False
	return hasLost, isBlackJack, score
		

def blackJack():
	reply = input("Do you want to play a game of Blackack? Type \"yes\" or \"no\": \n")
	while reply == "yes":
		playingDeck = newDeck()
		playerHand, dealerHand = [], []
		playerHand, dealerHand, playingDeck = startingPhase(playerHand, dealerHand, playingDeck)
		playerHasLost, playerBlackJack, playerScore = calculateHand(playerHand)
		dealerHasLost, dealerBlackJack, dealerScore = calculateHand(dealerHand)
		showHand(playerHand, playerScore)
		showHand(dealerHand, dealerScore, True, True)
		if playerBlackJack:
			print("BLACKJACK! You have won!")
		else:
			reply = input("Do want to draw a card? Type \"yes\" or \"no\": \n")
			while reply == "yes":
				playerHand, playingDeck = drawCard(playerHand, playingDeck)
				playerHasLost, blackJackHand, playerScore = calculateHand(playerHand)
				showHand(playerHand, playerScore)
				if playerHasLost:
					print("Your hand adds up to {}. You have lost.".format(playerScore))
					reply = "no"
				else:
					reply = input("Do want to draw a card? Type \"yes\" or \"no\": \n")
			if playerHasLost:
				break
			else:		
				showHand(playerHand, playerScore)
				showHand(dealerHand, dealerScore, True)
				if dealerBlackJack:
					print("The dealer has a BlackJack! You have lost.")
				else:	
					while dealerScore < playerScore and not dealerHasLost:
						print("Dealer is drawing a card...")
						time.sleep(3)
						playerHand, playingDeck = drawCard(dealerHand, playingDeck)	
						dealerHasLost, dealerBlackJack, dealerScore = calculateHand(dealerHand)
						showHand(dealerHand, dealerScore, True)
					if dealerHasLost:
						print("You have won!")
					else:
						print("Dealer wins, you have lost!")					
		reply = input("Do you want to play another round? Type \"yes\" or \"no\": \n")
		
			
if __name__ == "__main__":
	blackJack()
