# Explain what the program does.
print("") # Break to display a clean presentation.
print("This program will take a user supplied series of numbers and provide the Low, High, Total, and Average of the numbers input.")
print("") # Break to display a clean presentation.
# Declarations
notQuit = "Y"
numCount = []

# Start of loop with sentinel statement.
while notQuit == "Y":
    # Obtain the count of numbers the user wishes to use.
    numCount = int(input("How many numbers do you want? "))
    while numCount <= 0:
        numCount = int(input("You must enter a number greater than 0: ")) # Informs user if input is invalid.
    # Initialize the index to store the count of numbers.
    numVariable = [0] * numCount
    index = 0
    # Loop to run through the series of numbers to obtain the desired numbers to calculate.
    while index < numCount:
        print("Enter number ", index + 1, " of ", numCount, ": ", sep="", end="")
        numVariable[index] = float(input())
        index += 1 # Running through the index of numbers.

    # Calculations involving all of the numbers the user inputs.
    print("")
    minNum=min(numVariable)
    maxNum=max(numVariable)
    totalNum=sum(numVariable)
    averageNum=totalNum / numCount
    # Print sequences for output messages
    print("Here is the output")
    print("----------------------")
    print("Low: \t \t","{:.2f}".format(minNum))
    print("High: \t \t","{:.2f}".format(maxNum))
    print("Total: \t \t","{:.2f}".format(totalNum))
    print("Average: \t","{:.2f}".format(averageNum))
    print("")
    # Ask the user if they would like to start the program over with a new series of numbers.
    print("Do you want to enter another set of numbers?", end="")
    notQuit = input("Enter N to quit or Y to continue ")
    if notQuit == "N":
        print("Have a great day.") # Ends program if user prefers to quit.
        quit
