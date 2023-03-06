# The 'if' statement allows you to specify a condition and a block of code that will only be executed if the condition is true

# For example, the following code will check if the variable x is greater than 0, and if it is, it will print "x is positive"
x = 5
if x > 0:
    print("x is positive")

# We can also use the 'else' statement to specify a block of code that will be executed if the condition is false
x = -5
if x > 0:
    print("x is positive")
else:
    print("x is not positive")

# We can also use the 'elif' statement, which is short for 'else if', to specify more conditions
x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is 0")

# If statements can be used with user input
response = input("Are you in 50Five Capital (Y/N)? ")
# When checking if 2 values are equal to each other, you must use 2 equal signs (==), or else python will think we are trying to assign a variable
if response == "Y":
    print("Good to see you")
elif response == "N":
    print("Why are you here?")
else:
    print(response + " is not a valid response. Please enter Y or N.")
