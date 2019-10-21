
def main():

    print('Good morning.')

    payRate , hoursWorked = get_input()

    grossPay = payRate * hoursWorked

    print('Goodbye.', grossPay)

def get_input():

    payRate = float(input('Enter pay rate: '))

    hoursWorked = float(input('Enter hours worked: '))

    return payRate, hoursWorked

main()
