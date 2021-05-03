# Explain what the program will do.
print("This program will total the weekly sales.")

# Declarations
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
salesCount=[0] * 7

# Holding index
index = 0

# Initial loop to gather weekly sales totals.
while index < 7:
    print("Enter the sales for " + str(daysOfWeek[index]) + ": ", sep="", end="")
    salesCount[index] = float(input())
    while salesCount[index] <= -1:
        salesCount[index] = float(input("You must enter a number greater than or equal to 0: "))
    index += 1

# Outputs the total weekly sales.
total=sum(salesCount)
print("Total sales for the week: $"+ str (total))
