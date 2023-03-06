# In Python, a Collection is a special type of variable that can store multiple values.
# We will go over 3 different types of collections: lists, sets, and tuples.

# 1. Lists
# Lists are a collection of items, enclosed in square brackets []
# The items in a list can be of any data type and can be changed

fruits = ["apple", "banana", "orange"]  # create a list of fruits
print(fruits)  # Output: ["apple", "banana", "orange"]

# You can access the items of a list (aka "indexing") by using square brackets []
# Lists in most programming languages are zero-indexed, meaning the first item has an index of 0, the second item has an index of 1, and so on
print(fruits[0])  # Output: "apple" (access the first item in the list)
print(fruits[1])  # Output: "banana" (access the second item in the list)

# You can also use negative indexing to access items from the end of the list
print(fruits[-1])  # Output: "orange" (access the last item in the list)
print(fruits[-2])  # Output: "banana" (access the second last item in the list)

# These square brackets are known as the index operator [], and it has some other helpful features.
# The operator has 3 fields we can fill in: [start : end : step]
#   start: the start of the range we want to select. If you leave this empty, it will start at the first element in the list.
#   end: the end of the range we want to select. If you leave this empty, it will end at the last element in the list.
#   step: used to access every nth item in the list. If you leave this empty, it will default to 1, meaning it includes every item within the range provided.

# Let's see this in action.
fruits = ["apple", "banana", "orange", "mango", "kiwi"]
print(fruits[:2])  # Output: ["apple", "banana"] (access the first and second item)
print(fruits[1:3])  # Output: ["banana", "orange"] (access the second and third item)
print(fruits[::2])  # Output: ["apple", "orange", "kiwi"] (access every 2nd item in the list)
print(fruits[:4:2])  # Output: ['apple', 'orange'] (access every 2nd item in the list, in a range from the first to the third item)

# Lists are mutable, meaning their elements can be changed
fruits[0] = "mango"  # change the first item in the list to "mango"
print(fruits)  # Output: ['mango', 'banana', 'orange', 'mango', 'kiwi']

# Lists also have various useful built-in methods
fruits.append("coconut")  # adds an element at the end of the list
print(fruits)  # Output: ['mango', 'banana', 'orange', 'mango', 'kiwi', 'coconut']

fruits.insert(1, "grapes")  # inserts an element at a specific index
print(fruits)  # Output: ['mango', 'grapes', 'banana', 'orange', 'mango', 'kiwi', 'coconut']

fruits.remove("banana")  # removes an element from the list
print(fruits)  # Output: ['mango', 'grapes', 'orange', 'mango', 'kiwi', 'coconut']

# Just like strings, the len() function returns the number of elements in a list
# The reason this works is because strings are actually just lists of characters.
print(len(fruits))  # Output: 4


# 2. Sets
# Sets are collections of UNIQUE items, enclosed in curly braces {}. NO duplicates are allowed.
# Sets do not keep track of the order of items, meaning you cannot access a specific item by its index.
# You can add items to a set, but you cannot change ones that you already added

classes = {"Calculus", "Accounting", "Sociology"}  # Create a set of classes
print(classes)  # Outputs in a different order each time, since Python does not keep track of the order

# We use the add() method on a set to add another item
classes.add("Finance")  # Add "Finance" to the set
print(classes)  # Again, it outputs in a different order each time


# 3. Tuples
# Tuples are collections of items, enclosed in parentheses ()
# The items in a tuple cannot be modified and you cannot add new items. It is essentially locked.
# They do keep track of the order of items.

person = ("Anthony", "Butta", 21)  # create a tuple of Anthony's information
print(person)  # Output: ("Anthony", "Butta", 21)
