# Summary
# In this lab, you add a loop and the statements that
# make up the loop body to a Python program. When 
# completed, the program should calculate two totals:
# the number of left-handed people and the number of
# right-handed people in your class. Your loop should
# execute until the user eneters the character X instead
# of a L for left-handed or a R for right-handed.

# The inputs for this program are as follows:
# R, R, R, L, L, L, R, L, R, R, L, X
# Note that variables have been assigned for you, and 
# the input and output statements have been written for you.

# Instructions
# 1. Make sure the file LeftOrRight.py is selected and
# open.
# 2. Write a loop and a loop body that allows you to calculate
# a total of left-handed and a total of right-handed
# people in your class.
# 3. Execute the program using the Run bottom at the bottom
# at the bottoms of screen. Input the data listed above
# and verify that the output is correct.

rightTotal = 0  # Number of right-handed students.
leftTotal = 0  # Number of left-handed students.
leftOrRight = "R"
# Write your loop here.
while (leftOrRight == "L" or leftOrRight == "R"):
    leftOrRight = input("Enter an L if you are left-handed,a R if you are right-handed or X to quit.")
    if leftOrRight == "L":
        leftTotal = leftTotal + 1
    elif leftOrRight == "R":
        rightTotal = rightTotal + 1



# Output number of left or right-handed students.
print("Number of left-handed students: " + str(leftTotal))
print("Number of right-handed students: " + str(rightTotal))
