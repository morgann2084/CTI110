# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables

passes = 0  # number of passes

failures =0

num = int(input("How many students' results would you like to enter? ") )

# process 10 students

for student in range(num):


    result = int(input('Enter result (1=pass, 2=fail): '))
# get one exam result
    if result == 1:

        passes += 1
    else:

        failures +=  1



    print('Passed:', passes)
    print('Failed:', failures)

if passes >= 8:
    print('Bonus to instructor')
