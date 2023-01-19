# USERNAME VALIDATOR PROGRAM
# Create a program that prompts the user for a username and checks if it meets the following 3 criteria:
#   Username must be between 5 and 15 characters
#   Username does NOT contain spaces
#   Username does NOT contain numbers
# If the program does not meet one of the criteria, print an error message stating which criteria was not met.
# If the program meets all the criteria, print a "Username has been set" message.

# INSTRUCTIONS:
# Create a variable called username to store the user's input
# Use an if statement with the len() method and the "or" operator to check if the username is within the character length range.
#   Print an error message if it is out of bounds.
# Continue with an elif statement: use the "not" operator and the find() method to see if the username contains a space (" ").
#   Print an error message if the username contains a space.
#   Remember, the find() method returns -1 if it doesn't find what it's looking for.
# Continue with another elif statement: use the "not" operator and the isalpha() method to see if the username contains numbers
#   Print an error message if the username contains numbers.
# Finish with an else statement that prints the following success message: "Username has been set"


# SOLUTION:
username = input("Enter your username: ")

if len(username) <= 5 or len(username) >= 15:
    print("Error: username must be between 5 and 15 characters.")
elif not username.find(" ") == -1:
    print("Error: username must not contain spaces.")
elif not username.isalpha():
    print("Error: username must not contain numbers.")
else:
    print("Username has been set")
