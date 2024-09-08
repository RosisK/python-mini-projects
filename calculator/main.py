def main():
	while True:
		try:
			num1 = float(input("Enter first number: "))
		except ValueError:
			print("Invalid Input! Please enter a number.")
			continue

		operator = input("Enter an operator (+, -, *, /): ")
		while operator not in ['+', '-', '*', '/']:
			print("Invalid Input! Please enter an operator.")
			operator = input("Enter an operator (+, -, *, /): ")
		
		try:
			num2 = float(input("Enter second number: "))
		except ValueError:
			print("Invalid Input! Please enter a number: ")
			continue

		if operator == '/' and num2 == 0:
			print("Error: Division by zero is not allowed")
			continue

		operations = {
			'+': add,
			'-': subtract,
			'*': multiply,
			'/': divide
		}

		result = operations[operator](num1, num2)
		print(f"The result is: {result:.2f}")
		
		again = input("Do you want to perform another calculation? (yes/no): ")
		if again.lower() != 'yes':
			print("Program Terminated.")
			break;


def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

main()