# Dictionaries are an advanced collection that are comprised of pairs of keys and values.
# They can be modified but no duplicate keys are allowed.
# Some examples of key-value pairs are EMPLID and student names, state names and their capitals, product names and their prices, etc.

# To create a dictionary we use curly braces {} and a colon to separate values
capitals = {"New York": "Albany",
            "New Jersey": "Trenton",
            "California": "Sacramento"}
print(capitals)  # Output: {'New York': 'Albany', 'New Jersey': 'Trenton', 'California': 'Sacramento'}

# To retrieve a value from the dictionary, we use the get() function with the key
print(capitals.get("New York"))  # Output: Albany

# We can use the update() function to add new key-value pairs to the dictionary, or update existing ones
capitals.update({"Florida": "Tallahassee"})  # Add a "Florida" key to the dictionary
capitals.update({"New Jersey": "Hoboken"})  # Change the value for the "New Jersey" key to "Hoboken"
print(capitals)

# The get() method can also be used with an if statement
if capitals.get("Massachusetts"):  # If the key "Massachusetts" exists
    print(capitals.get("Massachusetts"))  # Print the value
else:  # If the key does not exist
    capitals.update({"Massachusetts": "Boston"})  # Add the key-value pair
    print(capitals)  # Print the new dictionary

# To remove a key-value pair, use the pop() method with the key you want to remove.
capitals.pop("Florida")  # Remove the "Florida" key and its value
print(capitals)  # Output: {'New York': 'Albany', 'New Jersey': 'Hoboken', 'California': 'Sacramento', 'Massachusetts': 'Boston'}

# We can get all the keys of a dictionary with the keys method, which returns a list of keys. That means we can iterate through it.
for key in capitals.keys():  # For each key in capitals
    print(key)  # Print the key

# We can do the same things for the values using the values() method, which also returns a list.
for value in capitals.values():  # For each value in capitals
    print(value)  # Print the value

# We can also use the items() method to iterate through both the keys and values simultaneously.
print(capitals.items())  # This returns a list of tuples, so our for loop needs 2 variables, separated by a comma

for key, value in capitals.items():  # For each key AND value in capitals
    print("The capital of " + key + " is " + value)  # Print both the key and value in a sentence

# The clear() method will clear the entire dictionary.
capitals.clear()
print(capitals)  # Output: {}
