# Summary
# In this lab, you add nested loops to a Python program
# provided. The program should print the outline of the
# letter E. The letter E is printed using asterisks, 
# three across and five down. This program uses the
# print("*", end-' ') to print an asterisk and 
# print(" ", end=' ') to print a space.

# Instructions
# 1. Write the nested loops to control the number of rows
# and the number of columns that make up the letter E, as
# shown below:
# ***
# *
# ***
# *
# ***
# 2. In the loop body, use a nested if statement to decide
# when to print an asterisk and when to print a space. The
# output statements have been written, but you must decide
# when and where to use them.
# Execute the program. Observe your output.

NUM_ACROSS = 3 # Number of asterisks to print across
NUM_DOWN = 5 # Number of asterisks to print down

for x in range(NUM_DOWN):# Write a loop to control the number of rows.
    for y in range(NUM_ACROSS):# Write a loop to control the number of columns
        if (x%2 == 0):# Decide when to print an asterisk in every column.
            print("*", end='')
        elif (y == 0):# Decide when to print asterisk in column 1.   
            print("*", end='')
        else:# Decide when to print a space instead of an asterisk.   
            print(" ", end='')
        # Figure out where to place this statement that prints a newline.
    print("\n")