"""
Writing Functions that Return a Value

Summary
In this lab, you complete a partially written Python program that includes a function that returns a value. The program is a simple calculator that prompts the user for two numbers and an operator ( +, -, *, or / ).

The two numbers and the operator are passed to the function where the appropriate arithmetic operation is performed. The result is then returned to where the arithmetic operation and result are displayed.

For example, if the user enters 3, 4, and *, the following is displayed:

3 * 4 = 12
The source code file provided for this lab includes the necessary input and output statements. Comments are included in the file to help you write the remainder of the program.

Instructions
Write the Python statements as indicated by the comments.
Execute the program.
"""

# Calculator.py - This program performs arithmetic, ( +. -, *. / ) on two numbers.
# Input:  Interactive
# Output:  Result of arithmetic operation

# Write performOperation function here
def performOperation(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y

if __name__ == '__main__':
    numberOne = int(input("Enter the first number: "))
    numberTwo = int(input("Enter the second number: "))
    operation = input("Enter an operator (+ - * /): ")

    # Call performOperation method here and store the value in "result"
    result = performOperation(numberOne, numberTwo, operation)
    print(str(numberOne) + " " + operation + " " + str(numberTwo) + " = " + str(result))
