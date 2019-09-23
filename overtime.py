# This program will calculate overtime pay.

# Ask the user to enter pay rate
payRate = float(input("What is your payrate? $"))

#Ask the user to enter the amount of hours worked
hoursWorked = float(input("How many hours have you worked?" ))

# Evaluate "if" statement

if hoursWorked > 40:
    overTime = (hoursWorked - 40) * payRate
    overPay = overTime * 1.5

    regHours = 40 * payRate
    grossPay = overPay + regHours
else:

    grossPay = hoursWorked * payRate

print("Your gross pay is ", grossPay, sep="")
    

