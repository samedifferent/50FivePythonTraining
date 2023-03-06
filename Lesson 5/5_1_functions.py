# A function is a block of code that can be reused.
# We have already used a lot of Python's built-in functions, like print(), type(), and len(), but we can also make our own!

# To create a function, we use the "def" keyword, followed by the function name, parentheses, and a colon
def about_me():
    print("My name is Andrew")
    print("I am 20 years old")
    print("I live in Manhattan")


# We can run our function by writing the function name followed by parentheses ()
about_me()


# That example is not very useful because the information can't be changed.
# We can pass information, known as "arguments" (or "parameters"), into the function and use them inside.
# We specify the arguments inside the parentheses, separated by commas
def about_me(name, age, location):
    print("My name is " + name)
    print("I am " + str(age) + " years old")
    print("I live in " + location)


# When we call the function, we can now specify arguments
about_me("Anthony Butta", 21, "Gravesend")


# It is perfectly fine to have multiple functions in the same file with the same name, as long as the arguments are different.

# We can also make a function that returns a value, which can be set to a variable or printed. We do this with the "return" keyword.
# Let's make a function to calculate net income.
def calc_net_income(revenue, expenses):
    return revenue - expenses


calc_net_income(500,
                200)  # Unlike the previous example, we shouldn't call our function like this because the result will just be ignored. We need to print it.
# Remember, values in our code will only appear in the console if we print them.
print(calc_net_income(500, 200))  # Output: 300

# We can also set the value equal to a variable
net_income = calc_net_income(500, 200)
print(net_income)  # Output: 300


# You can also call a function from inside itself. This is called recursion.
def walk(steps):  # This function takes in an argument of the total amount of steps we want to take
    # When we enter the function, we check if the steps reached zero
    if steps == 0:
        return  # A return statement with nothing afterwards can be used to exit a function, just like the break statement in a loop
    # If not, we call our walk function again from inside itself, but we pass in one less steps than the previous time
    walk(steps - 1)
    # Then print the current value of steps.
    print("You took step #" + str(steps))


walk(10)

# Python only supports recursion up to a certain limit, which is usually 1000. This will cause an error.
walk(1000)
