# This program will calculate and display the profit of total sales.
# 9/14/2019
# CTI-110 P2T1 - Sales Prediciton
# Nicolas Morgan

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
