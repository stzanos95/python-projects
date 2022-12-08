import random

HARD_GUESSES = 5
EASY_GUESSES = 10

def gameInit():
	print("Welcome to the Number Guessing Game!")
	print("I've just thought of a number between 1 and 100.")
	reply = input("Choose a difficulty. Type 'easy' or 'hard': \n")
	if reply == "easy":
		guesses = EASY_GUESSES
	else:
		guesses = HARD_GUESSES
	return guesses, random.randint(1, 100)		
	
def checkGuess(guess, secretNumber):
	
	if guess > secretNumber:
		print("Too high.")
		return False
	elif guess < secretNumber:
		print("Too low.")
		return False
	else:
		print("Correct! You have won.")
		return True
		
	 
def numberGuessing():
	attempts, solution = gameInit()
	guess = 0
	while guess != solution:
		print("You have {} attempts remaining to guess the number.".format(attempts))
		guess = int(input("Make a guess: \n"))
		hasWon = checkGuess(guess, solution)
		attempts -= 1
		if not hasWon:
			if attempts == 0:
				print("You have lost. The number was {}.".format(solution))
				break
			else:
				print("Guess again.")
		
if __name__ == "__main__":
	numberGuessing()
