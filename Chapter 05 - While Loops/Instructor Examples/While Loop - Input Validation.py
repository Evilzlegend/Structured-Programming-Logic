# This program displays gross pay.
# Get the number of hours worked.
hours = int(input("Enter the hours worked this week: "))

# Get the hourly pay rate.
payRate = float(input("Enter the hourly pay rate: "))

# Calculate the gross pay.
grossPay = hours * payRate

# Display the gross pay.
print("Gross pay: $",format(grossPay, ",.2f"))
