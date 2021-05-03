# This program calculates gross pay.
while True:
    try:
        # Get the number of hours worked.
        hours = int(input("How many hours did you work? "))
        while hours < 0:
            print("Please enter a value > 0")
            hours = int(input("Howw many hours did you work? "))
        # Get the hourly pay rate.
        payRate = float(input("Enter your hourly pay rate: "))
        while payRate < 0:
            print("Please enter a value > 0")
            payRate = float(input("Enter your hourly pay rate: "))
        break
    except ValueError:
        print("ERROR: Hours worked and hourly pay rate must be valid integers")

# Calculate the gross pay.
grossPay = hours * payRate
# Display the gross pay.
print("Gross pay: $", format(grossPay, ",.2f"), sep="")