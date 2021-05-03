# Ask the user what their income is.
income = int(input("What is your income? "))


# If the user's income is $20,000 or less use:
if income <= 20000:
    if income <= 20000:
        tax = income*(.02)
        print("Your tax rate is in the lowest tax bracket.")
        
# If the user's income is $50,000 or less use:
else:
    if income <= 50000:
        tax = 400+(.025)*(income-20000)
        print("Your tax rate is in the medium tax bracket.")
        
# If the user's income is more than $50,000 use:
    elif income > 50000:
        tax = 1150+(.035)*(income-50000)
        print("Your tax rate is in the highest tax bracket.")
# Inform the user what tax bracket they fall under and the taxes they pay.

print("Your tax rate is, $", format(tax, ",.2f"))
