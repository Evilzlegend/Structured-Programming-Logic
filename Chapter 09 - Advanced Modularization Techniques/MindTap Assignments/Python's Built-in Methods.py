"""
Python's Built-in Methods

Summary
In this lab, you complete a partially written Python program that includes built-in methods that convert Strings to all uppercase or all lowercase.

The program prompts the user to enter any string. To end the program, the user can enter "done". For each string entered, call the built in methods lower() and upper(). The program should call these methods using a string object, followed by a dot (.), followed by the name of the method. Both of these methods return a string with the string changed to uppercase or lowercase. Here is an example:

sample = "This is a String."
result = sample.lower(); 
result = sample.upper();
The source code file provided for this lab includes the necessary input and output statements. Comments are included in the file to help you write the remainder of the program.

Instructions
Make sure the file ChangeCase.py is selected and open.
Write the Python statements as indicated by the comments.
Execute the program by clicking on the Run button at the bottom of the screen.
"""

"""
ChangeCase.py - This program converts a string to lowercase and uppercase.
Input:  Interactive
Output:  Uppercase and lowercase versions of the user-entered string.
"""

sample = input("Enter a string or done when you want to quit: ")

while sample != "done":
    # Call the lower method here and print the result.
    result = sample.lower()
    print("Lowercase: " + result)
    # Call upper method here and print the result.
    result = sample.upper()
    print("Uppercase: " + result)
    sample = input("Enter a string or done when you want to quit: ")
