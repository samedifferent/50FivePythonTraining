# In this lesson, we will be going over some basic string methods in Python

# First, let's create a variable to hold a string
string = "Hello World!"

# Now, let's use the upper() method to convert the string to all uppercase
string = string.upper()
print(string)  # "HELLO WORLD!"

# We can also use the lower() method to convert the string to all lowercase
string = string.lower()
print(string)  # "hello world!"

# The replace() method can be used to replace a specific word or character in a string
# The method accepts 2 strings, the first is the one you want to find and the second is what you want to replace it with.
string = string.replace("world", "python")
print(string)  # "hello python!"

# The find() method can be used to find the index of the first occurrence of a specified value.
# It returns -1 as the index if the phrase is not found.
string = "Hello World!"
index = string.find("l")
print(index)  # 2

# The rfind() method, aka the "reverse find" method, finds the index of the last occurrence of a specified value.
# It returns -1 as the index if the phrase is not found.
string = "Hello World!"
index = string.rfind("l")
print(index)  # 9

# The index() method can be used to find the index of a specific word or character in a string.
# It works the same as the find() method, but it will raise an error if the word or character is not found
# There is also an rindex() method that works in reverse.
index = string.index("World")
print(index)  # 6

# The isdigit() method can be used to check if all characters in a string are numbers.
string = "12345"
print(string.isdigit())  # True

# The isalpha() method, aka the "is alphabet" method, can be used to check if all characters in a string are letters.
string = "Hello"
print(string.isalpha())  # True

# The len() function can be used to check the length of a string.
# This method is used a bit differently. The string goes inside of it.
print(len(string))  # 5

# There are way too many string methods to list here.
# A more comprehensive list can be found on this page: https://www.w3schools.com/python/python_strings_methods.asp
