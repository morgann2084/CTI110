# CTI 110
# 10/13/19
# Nicolas Morgan
# Turtle graphic tutorial pg. 180 Repeating Squares.

# import turtle

import turtle

turtle.right(180) # set direction

turtle.speed(0) # set speed to 0

length = 505

# Use 'for' loop and 'range' function

for times in range (100): # set 'range' to '100'

  for endtimes in range (4): # set 'range' to 4

    turtle.forward(length) # move turtle forward

    turtle.right(90)

  length -= 5
