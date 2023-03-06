# Logical operators are used with conditional statements to combine multiple conditions
# Python has 3 logical operators:
#   and = BOTH conditions must be true
#   or = ONE condition must be true
#   not = Inverts the condition, so true becomes false and false becomes true

# Let's see this with an example
temp = 60
rainy = True

if temp <= 32 and rainy:
    print("It will snow")
elif temp > 50 or not rainy:
    print("The weather is nice today")
else:
    print("It will rain")

