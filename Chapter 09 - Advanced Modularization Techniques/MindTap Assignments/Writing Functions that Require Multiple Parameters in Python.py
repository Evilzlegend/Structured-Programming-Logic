"""
Writing Functions that Require Multiple Parameters

Summary
In this lab, you complete a partially written Python program that includes a function requiring multiple parameters (arguments).

The program prompts the user for two numeric values. Both values should be passed to functions named calculateSum, calculateDifference, and calculateProduct. The functions compute the sum of the two values, the difference between the two values, and the product of the two values.

Each function should perform the appropriate computation and display the results. The source code file provided for this lab includes the variable declarations and the input statements.

Comments are included in the file to help you write the remainder of the program.

Instructions
Write the Python statements as indicated by the comments.
Execute the program.
"""

# Computation.py - This program calculates sum, difference, and product of two values.
# Input: Interactive
# Output: Sum, difference, and product of two values. 

# Write calculateSum function here
def calculateSum():
    sum = value1 + value2
    print(sum)
# Write calculateDifference function here
def calculateDifference():
    diff = value1 - value2
    print(diff)
# Write calculateProduct function here
def calculateProduct():
    prod = value1 * value2
    print(prod)
value1 = int(input("Enter first numeric value: "))
value2 = int(input("Enter second numeric value: "))
      
# Call calculateSum
calculateSum()
# Call calculateDifference
calculateDifference()
# Call calculateProduct
calculateProduct()
