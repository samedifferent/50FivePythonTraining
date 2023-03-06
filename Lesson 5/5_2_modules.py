# Modules are collections of functions and variables that can be used in your code.
# Python comes with many built-in modules to help us do things like more complex math, getting the current date/time, generating random numbers, and much more!

# We import modules using the "import" keyword.
# These import statements always go at the top of your python file, above all your other code.

# Let's import Python's random module to generate a random number
import random
# We can also import specific items from a module using the "from" keyword.
from math import sqrt  # Imports the sqrt (square root) function from the math module
# We can also import modules and give them a shorter nickname using the "as" keyword.
import datetime as dt  # Imports the datetime module with the nickname "dt"
# We can also create our own custom modules. Let's create one called "finance" with some helper financial methods.
import finance  # Imports the finance.py file that we just created

print(random.randint(1, 10))  # Generate a random number from 1 to 10
print(sqrt(9))  # Take the square root of 9
print(dt.datetime.now())  # Get the current date and time.
print(finance.net_income(500, 250))  # Call our net income function from the finance module
print(finance.gross_profit(500, 50))  # Call our gross profit function from the finance module
