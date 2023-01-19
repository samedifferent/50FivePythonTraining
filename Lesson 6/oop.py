# Python is an object oriented programming (OOP) language. You can think of an object as a thing with properties and behaviors.
# Classes are blueprints for creating these objects. It is easiest to illustrate this with an example.

# First, we'll create a class called "Stock". This class will represent a stock and have properties such as the stock's symbol, name, and current price.
# We can create a class with the "class" keyword. Class names generally begin with a capital letter.

class Stock:
    # Let's add some relevant properties to the stock class.
    symbol = None
    name = None
    price = None

    # We can also add a function to the class. Functions that are part of a class are known as methods.
    # Let's add a method to calculate the value of the stock.
    # We need to add a "self" argument, which refers to the current object of the class and is used to access the object's properties, like the price.
    # We will also add an argument called "shares" which represents the number of shares of the stock the user owns.
    def get_value(self, shares):
        return self.price * shares  # Returns the total value of the stock by multiplying the price of the stock by the number of shares.

    # The last thing we need for our class is a special method: the __init__ method.
    # The __init__ method is called when an object of the class is created. It is also known as a "constructor".
    # It lets us set the initial values for the object's properties, which in this case are the symbol, name, and price of the stock.
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price


# Now that we have a class, we can create objects of the class and set their properties.
apple = Stock("AAPL", "Apple Inc.", 132.50)
google = Stock("GOOGL", "Alphabet Inc.", 1823.50)

# Here we created two objects of the class Stock, one for Apple and one for Google, and set their respective symbol, name, and price.
# We can use the get_value method to get the value of the stock objects we just created.
print(apple.get_value(100))  # prints the value of the apple stock if we own 100 shares
print(google.get_value(100))  # prints the value of the google stock if we own 100 shares


# Perhaps the most important concept of object oriented programming is inheritance.
# If we want to create a class that is similar to another class without having to rewrite everything from scratch, we can use inheritance.
# Let's create a class called "IndexFund" that inherits from the Stock class.

# To let Python know we want to inherit from the Stock class, we add parentheses after the class name and put the Stock class inside
class IndexFund(Stock):
    # The IndexFund class inherits from the Stock class and has all the properties and methods of the Stock class.
    # We still need to add an __init__ method, but this time let's add new property called "index" which represents the index the fund is tracking (for example, the S&P500).
    def __init__(self, symbol, name, price, index):
        self.index = index  # Set the initial value of the index property
        # When inheriting, we must use the super() function to call the __init__ method of the parent class (Stock) and pass in the symbol, name, and price.
        super().__init__(symbol, name, price)


# Now we can create an object of the IndexFund class and use its properties and methods.
spy = IndexFund("SPY", "SPDR S&P 500 ETF", 389.98, "S&P500")
print(spy.get_value(100))  # prints the value of the SPY stock if we own 100 shares
