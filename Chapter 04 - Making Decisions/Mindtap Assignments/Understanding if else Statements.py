# LargeSmall.py - This program calculates the largest and smallest of three integer values. 
# Declare and initialize variables here
firstNumber = -50;
secondNumber = 53;
thirdNumber = 78;

# Write assignment, if, or if else statements here as appropriate
if firstNumber > secondNumber:
    if firstNumber > thirdNumber:
        largest = firstNumber
elif secondNumber > thirdNumber:
    if secondNumber > firstNumber:
        largest = secondNumber
else:
    largest = thirdNumber

if firstNumber < secondNumber:
    if firstNumber < thirdNumber:
        smallest = firstNumber
elif secondNumber < thirdNumber:
    if secondNumber < firstNumber:
        smallest = secondNumber
else:
    smallest = thirdNumber

# Output largest and smallest number. 
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))
