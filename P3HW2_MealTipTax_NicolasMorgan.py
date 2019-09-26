# CTI-110
# P3HW2 - MealTipTax
# Nicolas Morgan 
# 9-25-19
# This program will calculate meal cost, tip percentage, and tax.

# Sales tax is 6%
# User has a choice of 16% or 18% or 20% tip.

# Ask the user to enter meal cost.

mealCost = float(input("How much did your meal cost? $"))

# Ask the user to enter tip amount they would like to consider (16% or 18% or 20%)

tip = float(input("How much would you like to tip? (%16 or %18 or %20): %"))

# Evaluate using if/elif statements.

if tip == 16:
    print("You tipped %16.")

elif tip == 18:
    print("You tipped %18.")

elif tip == 20:
    print("You tipped %20.")

# Display an error message if user enters incorrect amount.

else:
    print("Incorrect amount. Enter %16 or %18 or %20.")

# Use def fucntion to return an argument.
    
    def enterAgain():
        
        float(input("How much would you like to tip? (%16 or %18 or %20): %"))
        
    enterAgain()

# Declare tip variables.
    
tip = 0.16 or 0.18 or 0.2 * mealCost

# Declare tax variable.

salesTax = 0.06 * mealCost

# Calculate total meal cost + tip + tax

total = mealCost + (mealCost * tip) + (mealCost * salesTax)

# Display total cost of meal (food charge + tip + tax)

print("Your total is: $ %.2f" % total)









