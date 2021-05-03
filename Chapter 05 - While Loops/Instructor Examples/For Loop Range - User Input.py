# Get the starting value.
print("This program displays a list of numbers")
print("and their squares.")
start = int(input("Enter the starting number: "))

# Get the ending limit.
end = int(input("How high should I go? "))

#Print the table headings.
print()
print("Number\tSquares")
print("---------------")

# Print the numbers and their squares.
# The +1 makes the end number reach the user's
# desired end number.
for number in range(start, end +1):
    square = number**2
    print(number, "\t", square)
