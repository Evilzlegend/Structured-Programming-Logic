# This program prompts the user for sales amounts
# and writes those amounts to the sales.txt file.

# Get the number of days.
numDays = int(input("For how many days do " + \
                    "you have sales? "))

# Open a new file named sales.txt.
salesFile = open("sales.txt", "w")

# Get the amount of sales for each day and writes# it to the file.
for count in range(1, numDays + 1):
    # Get the sales for a day.
    sales = float(input("Enter the sales for day #" + \
                        str(count) + ": "))

    # Write the sales amount to the file.
    salesFile.write(str(sales) + "\n")

# Close the file.
salesFile.close()
print("Data written to sales.txt.")