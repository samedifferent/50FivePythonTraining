# Loops are a way we can run a block of code multiple times.
# Python has 2 types of loops.

# 1. While loop
# The while loop will repeat a block of code as long as a certain condition is true

x = 0  # initialize x to 0

while x < 5:  # while x is less than 5
    print(x)  # print the current value of x
    x += 1  # increment x by 1

# Output: 0 1 2 3 4

# A common use of the while loop is with the input statement, to make sure the user enters what we want

age = input("Enter your age: ")  # Ask the user for their age

while age == "" or age.isalpha():  # While the user's input is empty or their input was not a number
    print("You did not enter your age properly")  # Tell the user they did not enter their age properly
    age = input("Enter your age: ")  # Ask the user again to enter their age.

print("You are " + age + " years old")

# 2. For loop
# The for loop is used to iterate over a collection (such as a list or string, since strings are just lists of characters)

colors = ["red", "blue", "green"]  # create a list of colors

for color in colors:  # for each color in the list
    print(color)  # print the color

# Output: red blue green

# You can also use the range function to create a range of numbers to iterate over
# The range function creates a range from 0 (inclusive) to the number you enter (exclusive).
for i in range(3):  # for each number i in the range 0-2
    print(i)  # print the current value of i

# Output: 0 1 2

# The range function can also take in 2 numbers to create a range.
for i in range(3, 6):  # for each number i in the range 3-5
    print(i)  # print the current value of i

# Output: 3 4 5

# You can use the "break" keyword anywhere inside a while or for loop to instantly break out of the loop.
# This can be helpful when you want to repeatedly take user input.

attendance_list = []
while True:  # This makes the loop run forever (unless we break out of it)
    name = input("Enter your name (Enter q to quit): ")  # Ask the user for a name, with the option to quit
    if name == "q":  # If the user enters q to quit
        break  # Break out of the loop
    else:
        attendance_list.append(name)  # Add the name to the attendance list

print(attendance_list)