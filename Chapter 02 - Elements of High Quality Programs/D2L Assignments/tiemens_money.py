# Entering the desire amount.
dollarAmount = float(input("Please enter your dollar amount: "))

# The federal tax taken from amount.
federalTax=.075

# The local tax taken from amount.
localTax=.03

# The amount of federal tax taken from amount.
saleFederal=dollarAmount*federalTax

# The amount of local tax taken from amount.
saleLocal=dollarAmount*localTax

# The total outcome of it all.
totalOutcome=dollarAmount-saleFederal-saleLocal

print("The dollar amount you entered was: ",dollarAmount)
print("Amount of federal tax withheld: ",(format(saleFederal,'.2f')))
print("Amount of local tax withheld: ",(format(saleLocal,'.2f')))
print("Your total is: ",(format(totalOutcome,'.2f')))
