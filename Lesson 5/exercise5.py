# Let's create a program that converts angles from degrees to radians and vice versa

# INSTRUCTIONS:
# Import the pi variable from the math module.
# Define a function called deg_to_rad that takes in a value in degrees and returns the value in radians (Multiply by pi / 180)
# Define a function called rad_to_deg that takes in a value in radians and returns the value in degrees (Multiply by 180 / pi)
# Create a variable called "angle" that prompts the user to enter an angle, and cast their response to a float
# Create a variable called "unit" that asks the user if the angle that they entered is in D or R.
# Use an if statement that calls the corresponding function and prints that value to the user. If the user did not enter D or R, print an error message.


# SOLUTION:

from math import pi


def deg_to_rad(degrees):
    return degrees * pi / 180


def rad_to_deg(radians):
    return radians * 180 / pi


angle = float(input("Enter an angle to convert: "))
unit = input("Is your angle in degrees or radians (Enter D or R)? ")

if unit == "D":
    print(deg_to_rad(angle))
elif unit == "R":
    print(rad_to_deg(angle))
else:
    print(unit + " is not a valid unit.")
