# To take input from the user, we can use the built-in function input()
# The input function takes in a string, which is the prompt that we want to display to the user

# For example, to ask the user for their name:
name = input("What is your name? ")
# The input function returns a string, so the variable 'name' will be a string containing the user's input
# We can then use this variable in our program
print(name + " is in 50Five Capital")

# We can also use type casting to convert the user's input to a different data type if needed, such as an integer
semesters = int(input("How many semesters have you completed so far? "))
semesters_remaining = 8 - semesters
print(name + " has " + str(semesters_remaining) + " semesters until graduation.")


