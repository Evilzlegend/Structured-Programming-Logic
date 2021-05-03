# User Input
num = float(input("Enter a positive number (negative to quit): "))

# Initialize Total
total = 0.0

# Loops through number until a negative number is entered.
while num > 0:
    total = num + total
    num = float(input("Enter a positive number (negative to quit): "))

# Print answer.
print("Total =",format(total, '.2f'))