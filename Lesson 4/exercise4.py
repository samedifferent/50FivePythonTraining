# Let's create a portfolio manager program.
# This program will first let the user add stock symbols and their prices to a portfolio.
# When the user is done adding stocks, the program will print out each stock symbol and its value.

# INSTRUCTIONS:
# Create an empty dictionary variable called "portfolio"
# Create an infinite while True loop. Inside the loop, create a symbol variable that prompts the user to enter a stock. The prompt should include an option to press a letter to quit.
# Use an if statement to check if the user pressed the quit letter, and if so, break out of the loop.
#   If not, create a price variable that prompts the user to enter the stock's price.
#   Then update the dictionary with the symbol and price
# Add a for loop that iterates through the keys and values of the dictionary, printing a sentence saying "The value of (key) is (value)"

# SOLUTION
portfolio = {}

while True:
    symbol = input("Enter a stock symbol (Press q to quit): ")
    if symbol == "q":
        break
    else:
        price = input("Enter the stock's price: ")
        portfolio.update({symbol: price})

for key, value in portfolio.items():
    print("The value of " + key + " is " + str(value))
