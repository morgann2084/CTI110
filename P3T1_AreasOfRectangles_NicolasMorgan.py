
# This program will calculate the area of a rectangle.

# Get dimensions of rectangle 1.

length1 = int(input("Enter the length of rectangle 1: "))

width1 = int(input("Enter the width of rectangle 1: "))

# Get dimensions of rectangle 2.

length2 = int(input("Enter the length of rectangle 2: "))

width2 = int(input("Enter the width of rectangle 2: "))

# Calculate the areas of the rectangles.

area1 = length1 * width1

area2 = length2 * width2

# Determine which has the greatest area.

if area1 > area2:
    print("Rectangle1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both have the same area.")
