
# CTI-110
# P3LAB - Debugging
# Nicolas Morgan 
# 9-25-19
# This is a debugging exercise that will correct aligment and indentation in a program.

# Original program

# if score >= A_score:
# print('Your grade is A.')
# else:
# if score >= B_score:
# print('Your grade is B')
# else:
# if score >= C_score:
# print('Your grade is C')
# else:
# if score >= D_score:
# print('Your grade is D')
# else:
# print('Your grade is F')

# Corrected program with proper indents and aligment.

score = float(input("Enter score: "))

if score >= 90:
    print('Your grade is A.') #indent 'print'
else:

    if score >= 80: # indent 'if' under 'else:'
        print('Your grade is B')
    else: #align 'else:' under 'if'

        if score >= 70:
            print('Your grade is C')
        else:

            if score >= 60:
                print('Your grade is D')
            else:
                print('Your grade is F')


