"""
Optional Arguments in Functions

Summary
In this lab, you complete a partially written Python program that computes hotel guest rates at Cornwall’s Country Inn.

The program is described in Chapter 9, Exercise 11, in Programming Logic and Design. In this program, you should include a function named computeRate(). It should accept the number of days and calculate the rate at $99.99 per day.

It should optionally include a code for a meal plan. If the code is A, three meals per day are included, and the price is $169.00 per day. If the code is C, breakfast is included, and the price is $112.00 per day. All other codes are invalid.

The function returns the rate to the calling program where it is displayed. The main program asks the user for the number of days in a stay and whether meals should be included; then, based on the user’s response, the program either calls the function or prompts for a meal plan code and calls the function. Comments are included in the file to help you write the remainder of the program.

Instructions
Make sure the file Cornwall.py is selected and open.
Write the Python statements as indicated by the comments.
Execute the program by the clicking the Run button at the bottom of the screen.
"""

# Cornwall.py - This program computes hotel guest rates.
# Input:  Days in stay and meals included
# Output:  Hotel guest rate

# Write computeRate function here
def computeRate(days, code="0"):
    if code == "A":
        return 169 * days
    elif code == "C":
        return 112 * days
    else:
        return days * 99.99


if __name__ == '__main__':
    rate = 0
    dayString = input("How many days do you plan to stay? ")
    days = int(dayString)
    question = input("Do you want a meal plan? Y or N ")
    if question == "Y":
        code = input("Enter A for 3 meal plan, or C for only breakfast plan: ")
        rate = computeRate(days, code)
    else:
        rate = computeRate(days)
    print("The rate for your stay is: {:.2f}". format(rate))
    # Figure out which arguments to pass to the computeRate() function and 
    # then call the computeRate() function
    computeRate(rate)
    
