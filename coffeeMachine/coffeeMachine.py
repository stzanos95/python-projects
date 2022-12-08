from coffeeData import *

print("Welcome to Tzanos Coffee and chill!")

def makeCoffee(coffee):
	hasResources, lessResources = checkResources(coffee)
	if hasResources:
		inputMoney = processCoins()
		while inputMoney < menu[coffee]["price"]:
			print("You have not entered enough currency. The price is: ${} \nTry again.".format(menu[coffee]["price"]))
			inputMoney = processCoins()
		else:
			addMoney(inputMoney)
			removeResources(coffee)
			print("Here is your change: ${}".format(inputMoney - menu[coffee]["price"]))
	else:
		print("Sorry, we've run out of: {}".format(", ".join(lessResources)))
	
def checkResources(coffee):
	lessResources = []
	for resource, value in resources["resources"].items():
		if value["value"] - menu[coffee][resource] < 0:
			lessResources.append(resource)
	if len(lessResources) > 0:
		hasResources = False
	else:
		hasResources = True
	return hasResources, lessResources
	
def processCoins():
	print("Please insert coins.")
	inputMoney = int(input("How many quarters? ")) * 0.25
	inputMoney += int(input("How many dimes? ")) * 0.10
	inputMoney += int(input("How many nickels? ")) * 0.05
	inputMoney += int(input("How many pennies? ")) * 0.01
	print("You have inserted: ${}".format(inputMoney))
	return inputMoney
	
def addMoney(money):
	resources["money"] += money
	
def removeResources(coffee):
	for resource, value in resources["resources"].items():
		value["value"] -= menu[coffee][resource]
	
def makeReport():
	print("Machine resources:")
	for resource, value in resources["resources"].items():
		print("{}: {}{}".format(resource.title(), value["value"], value["unit"]))
	print("Money: ${}".format(resources["money"]))
	
def coffeeMachine():
	atCoffeeMachine = True
	while atCoffeeMachine:
		selection = input("If you would like a coffee, type 'espresso', 'latte' or 'cappuccino'.\nElse, type 'leave'\n")
		if selection == 'off':
			atCoffeeMachine = False
		elif selection == 'report':
			makeReport()
		elif selection in menu.keys():
			print("You have selected a {}. The price is: ${}".format(selection, menu[selection]["price"]))
			makeCoffee(selection)
		elif selection == 'leave':
			atCoffeeMachine = False
		else:
			print("This is not a valid command. Try again.")		


if __name__ == "__main__":
	coffeeMachine()
