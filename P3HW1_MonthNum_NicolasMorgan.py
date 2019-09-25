
# CTI-110
# P3HW1 - Month Number
# Nicolas Morgan
# 9-25-19
# This program will determine what month it is based on a number the user enters from 1 to 12.

# Ask the user to enter a number from 1-12.

number = int(input("Enter a number from 1 through 12. "))

# Evaluate using if/elif statements.

if number == 1:
    print("January")

elif number == 2:
    print("February")

elif number == 3:
    print("March")

elif number == 4:
    print("April")

elif number == 5:
    print("May")

elif number == 6:
    print("June")

elif number == 7:
    print("July")

elif number == 8:
    print("August")

elif number == 9:
    print("September")

elif number == 10:
    print("October")

elif number == 11:
    print("November")

elif number == 12:
    print("December")

else:
    print("Incorrect number! Please enter a number 1 through 12.")
