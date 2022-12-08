def operate(a, b, operator):
	if operator == "+":
		result = round(addition(a, b), 3)
	elif operator == "-":
		result = round(subtraction(a, b), 3)
	elif operator == "*":
		result = round(multiplication(a, b), 3)
	else:
		result = round(division(a, b), 3)
	print("{} {} {} = {}".format(a, operator, b, result))
	return result

def addition(a, b):
	return a + b

def subtraction(a, b):
	return a - b

def multiplication(a, b):
	return a * b
	
def division(a, b):
	return a / b
	
def interface(prev_num=0, reuse=False):
	if reuse:
		x = prev_num
	else:
		x = float(input("What's the first number? \n"))
	oper = input("Pick an operation (+, -, *, /) \n")
	while oper not in "+-*/":
		oper = input("Invalid operation symbol. Please pick a valid operation symbol (+, -, *, /): \n")
	y = float(input("What's the second number? \n"))
	while oper == "/" and y == 0:
		y = float(input("Cannot divide by zero. Please select another number: \n"))
	result = operate(x, y, oper)
	reply = input("Continue calculating? Type \"yes\" or \"no\": \n") 
	if reply == "yes":
		reply = input("Use the result as first input? Type \"yes\" or \"no\": \n")
		if reply == "yes":
			interface(prev_num=result, reuse=True)
		else:
			interface()
	else:
		return False
		
def calculator():
	print("--> Welcome to the CALCULATOR <--")
	isCalculating = True
	while isCalculating:
		isCalculating = interface()
	print("Ciao!")
	
if __name__ == "__main__":
	calculator()
