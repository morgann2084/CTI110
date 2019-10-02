
# Create a variable to control the loop.

start_over = 'y'

while start_over == 'y': 

# Ask the employee's name.

    name = input('Please enter your name: ' )

# Ask the user to enter the pay rate.

    payRate = float(input('Please enter your pay rate: ' ))

# Ask the user to enter hours worked.

    hoursWorked = float(input('How many hours have you worked? '))

# If else

    if hoursWorked > 50:
        overTime = (hoursWorked - 50) * payRate
        overPay = overPay * 1.5

        regHours = 50 * payRate
        grossPay = overPay + regHours

    else:
        grossPay = hoursWorked * payRate

# Display gross pay.

    print('Your gross pay is ', grossPay, sep='')

    start_over = input('Do you want to run the program again? ' + 'grossPay (Enter y for yes): ')



