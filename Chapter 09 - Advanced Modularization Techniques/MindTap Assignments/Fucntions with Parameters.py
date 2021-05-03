"""
Functions with Parameters

Summary
In this lab, you complete a partially written Python program that includes two functions that require a single parameter.

The program continuously prompts the user for an integer until the user enters 0. The program then passes the value to a function (sums) that computes the sum of all the whole numbers from 1 up to and including the entered number. Next, the program passes the value to another function (products) that computes the product of all the whole numbers up to and including the entered number.

The source code file provided for this lab includes the necessary input statement. Comments are included in the file to help you write the remainder of the program.

Instructions
Make sure the file SumAndProduct.py is selected and open.
Write the Python statements as indicated by the comments. Remember to output the sum and product to the console.
Execute the program by clicking the Run button at the bottom of the screen.
"""


"""
SumAndProduct.py - This program computes sums and products.
Input:  Interactive.
Output:  Computed sum and product.
"""


# Write sums() function here.
def sums(num):
    sum = 0
    for i in range (num + 1):
        sum = sum + i 
    print(sum)

# Write products() function here.
def products(num):
    products = 1
    for i in range (1, num + 1):
        products = products * i
    print(products)

numberString = input("Enter a positive integer or 0 to quit: ")
number = int(numberString)

while number != 0:
    # Call sums() function here.
    sums(number)
    # Call products() function here.
    products(number)
    numberString = input("Enter a positive integer or 0 to quit: ")
    number = int(numberString)
