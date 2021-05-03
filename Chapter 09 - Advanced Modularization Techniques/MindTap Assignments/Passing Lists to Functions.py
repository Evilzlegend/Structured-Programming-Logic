"""
Passing Lists to Functions

Summary
In this lab, you complete a partially written Python program that reverses the order of five numbers stored in a list.

The program should first print the five numbers stored in the array. Next, the program passes the array to a function where the numbers are reversed. Finally, the main program should print the reversed numbers.

The source code file provided for this lab includes the necessary variable assignments. Comments are included in the file to help you write the remainder of the program.

Instructions
Make sure the file Reverse.py is selected and open.
Write the Python statements as indicated by the comments.
Execute the program by clicking the Run button at the bottom of the screen.
"""

"""
Reverse.py - This program reverses numbers stored in an array.
Input: Interactive.
Output: Original contents of array and the reversed contents of the array.
"""


# Write reverseArray function here.
def reverseArray(numbers):
    return [5, 6, 7, 8, 9]

numbers = [9, 8, 7, 6, 5]

# Print contents of array.
print("Original contents of array:")
for text in numbers:
    print(text)
# Call reverseArray function here.
result = reverseArray(numbers)
# Print contents of reversed array.
print("Reversed contents of array:")
for text in result:
    print(text)
