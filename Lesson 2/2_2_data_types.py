# What types of data can variables store?
# - integers
# - floats
# - strings
# - booleans

# Let's start with integers, which are simply whole numbers.
revenue = 500
print(revenue)  # Output: 500

# Python gives us a type function to determine the data type of a variable.
print(type(revenue))  # Output: <class 'int'>

# Next, let's look at floats, which are decimal numbers.
pi = 3.14
print(pi)  # Output: 3.14
print(type(pi))  # Output: <class 'float'>

# Strings are used to store text and are denoted by either single or double quotes.
name = "50Five"
print(name)  # Output: 50Five
print(type(name))  # Output: <class 'str'>
# You can also combine (concatenate) strings like so:
print("The name of this club is " + name)  # Output: The name of this club is 50Five

# Booleans are used to represent true or false values. They MUST be written with a capital T or F.
profitable = True
print(profitable)  # Output: True
print(type(profitable))  # Output: <class 'bool'>
