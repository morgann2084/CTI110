# This program will calculate the total amount of a meal purchased at a restaurant.
# 9/14/2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Nicolas Morgan

# The tip is 15%
# The sales tax is 6%

# Ask user to enter meal cost
mealCost = float(input("How much does your meal cost? $"))

# Ask the user to enter tip amount
tip = float(input("Please enter the tip amount: $"))
tip = 0.15 * mealCost

# Ask the user to enter tax amount
salesTax = float(input("Please enter the tax amount: %"))
salesTax = 0.06 * mealCost

# Calculate total meal cost + tip + tax
total = mealCost + (mealCost * 0.15) + (mealCost * 0.06)

# Display total cost of meal (food charge + tip + tax)
print("Food Charge: $ %.2f" % total)
