# INSTRUCTIONS:
# Create a calculator program that can perform the 4 basic math functions.
# Ask the user to input their first number, and store it in a variable.
# Ask the user to input their second number, and store it in a different variable.
# Ask the user which operator (+, -, *, /) they would like to use on the numbers, and store it in a variable.
# Use a chain of if/ifel/else statements to print the appropriate result.
# If the user did not enter one of those 4 valid operators, print an error message to the user with their input concatenated with the phrase " is not a valid operator".


# SOLUTION

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
op = input("Enter one of the following 4 operators (+, -, *, /): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print(op + " is not a valid operator")
