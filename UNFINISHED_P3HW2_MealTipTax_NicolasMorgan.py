
# CTI-110
# P3HW2 - MealTipTax
# Nicolas Morgan 
# 9-25-19
# This program will calculate meal cost, tip percentage, and tax.

# Sales tax is 6%
# User has a choice of 16% or 18% or 20% tip.

# Ask the user to enter meal cost.

mealCost = float(input("How much does your meal cost? $"))

# Ask the user to enter tip amount they would like to consider (16% or 18% or 20%)

tip = float(input("Tip amount: For 16% enter 0.16 or 18% enter 0.18 or 20% enter 0.2? %"))

def main():
    if tip == 0.16:
        print("Your tip is 16%.")

    elif tip == 0.18:
        print("Your tip is 18%.")

    elif tip == 0.2:
        print("Your tip is 20%.")

    else:
        print("Invalid amount, please enter tip amount of 16% or 18% or 20%.")

main()
