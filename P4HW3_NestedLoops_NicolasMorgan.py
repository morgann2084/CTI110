# This program will use nested loops to draw a pattern.
# 10/13/19
# CTI-110 P4HW3 - Nested Loops
# Nicolas Morgan

# Use "for" loop and "range" fucntion

for row in range( 6 ): # number of rows in this pattern

    print( "#", end="", sep="" ) # print the first '#' in each row

    for spaces in range( row ): # use inner loop to print spaces

        print( " ", end="", sep="" )

    print( "#", sep="" ) # print the last '#' in each row
