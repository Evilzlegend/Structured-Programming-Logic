"""
Functions with No Parameters

Summary
In this lab, you complete a partially prewritten Python program that includes a function with no parameters.

The program asks the user if they have preregistered for art show tickets. If the user has preregistered, the program should call a function named discount() that displays the message "You are preregistered and qualify for a 5% discount." If the user has not preregistered, the program should call a function named noDiscount() that displays the message "Sorry, you did not preregister and do not qualify for a 5% discount."

The source code file provided for this lab includes the necessary input statement. Comments are included in the file to help you write the remainder of the program.

Instructions
Make sure the file ArtShow.py is selected and open.
Write the Python statements as indicated by the comments.
Execute the program by clicking the Run button at the bottom of the screen.
"""


"""
ArtShow.py - This program determines if an art show
attendee gets a 5% discount for pre-registering.
Input: Interactive.
Output: A statemtne telling the user if they get a discount or no discount.
"""


# Write discount function here.
def discount():
    print("You are pre-registered and qualify for a 5% discount.")

# Write noDiscount function here.
def noDiscount():
    print("Sorry, you did not pre-register and do not qualify for a 5% discount.")

if __name__ == '__main__':
    registerString = input("Did you pre-register? Enter Y or N: ")

    # Test input here. If Y, call discount(), else call noDiscount().
    if registerString == "Y":
        discount()
    else:
        noDiscount()