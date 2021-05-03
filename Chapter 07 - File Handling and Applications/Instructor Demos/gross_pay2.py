# This program calculates gross pay.

try:
    # Get the number of hours worked.
    hours = int(input("How many hours did you work? "))

    # Get the hourly pay rate.
    payRate = float(input("Enter your hourly pay rate: "))

    # Calculate the gross pay.
    grossPay = hours * payRate
    # Display the gross pay.
    print("Gross pay: $", format(grossPay, ',.2f'), sep="")

    
except ValueError:
    print("ERROR: Hours worked and hourly pay rate must")
    print("be valid integers.")

else:

    # Calculate the gross pay.
    grossPay = hours * payRate

    # Display the gross pay.
    print("Gross pay: $", format(grossPay, ",.2f"), sep="")