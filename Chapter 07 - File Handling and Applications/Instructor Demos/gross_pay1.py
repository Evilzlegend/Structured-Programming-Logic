# This program calculates gross pay.


# Get the number of hours worked.
hours = int(input("How many hours did you work? "))

# Get hourly pay rate.
payRate = float(input("Enter your hourly pay rate: "))

# Calculate the gross pay.
grossPay = hours * payRate
# Display the gross pay.
print("Gross pay: $", format(grossPay, ',.2f'), sep="")