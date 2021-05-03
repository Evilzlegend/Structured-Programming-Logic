# Sentinel Variable
notQuit = "Y"

# Check for Sentinel Variable
while notQuit == "Y":
    # Input number
    num = int(input("Enter a positive nonzero number: "))
    total = 0
    # If number is zero or negative
    while num <= 0:
        num = int(input("Invalid. Enter a positive nonzero number: "))
    # Loop to add all the numbers together
    for count in range(1, num + 1):
        total = total + count
    # Print
    print("The sum of all the integers from 1 to", num ,"is",total)
    # Loop for continuing with another number
    notQuit = input("Do you want to enter another number? (Y or N)")
    if notQuit == "N":
        print("Have a great day!")