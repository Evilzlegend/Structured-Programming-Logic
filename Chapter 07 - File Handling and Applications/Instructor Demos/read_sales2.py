# This program uses the for loop to read
# all of the values in the sales.txt file.

# Open the sales.txt file for reading.
salesFile = open("sales.txt", 'r')

# Read all the lines from the file.
for line in salesFile:
    # Convert line to a float.
    amount = float(line)
    # Format and display the amount.
    print(format(amount, '.2f'))

# Close the file.
salesFile.close()