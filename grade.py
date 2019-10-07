
# This program will use a while loop to ask the user to enter grades.

# Create a variable to control the loop.

count = 0

total = 0

grade = float(input('Enter your grade or -1 to end program '))

while grade != -1:
    total = total + grade
    count = count +1


    grade = float(input('Enter your grade or -1 to end program '))

avg = total / count

print('Your average is:, ', avg)
    

    





    
