import random

def numToObject(num):
    if num == 0:
        return "Rock"
    elif num == 1:
        return "Paper"
    else:
        return "Scissors"

user_choice = input("What do you want to choose? Type: \n0 for Rock \n1 for Paper \n2 for Scissors \n")

print("You chose: " + numToObject(user_choice))
print("-----------------------")
comp_choice = random.randint(0, 2)
print("The computer chose: " + numToObject(comp_choice))

if user_choice == comp_choice:
    print("It's a tie.")
elif user_choice == 0:
    if comp_choice == 1:
        print("You lose!")
    elif comp_choice == 2:
        print("You win!")
elif user_choice == 1:
    if comp_choice == 0:
        print("You win!")
    elif comp_choice == 2:
        print("You lose!")
elif user_choice == 2:
    if comp_choice == 0:
        print("You lose!")
    elif comp_choice == 1:
        print("You win!")
