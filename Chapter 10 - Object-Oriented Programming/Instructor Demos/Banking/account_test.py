# This program demonstrates the BankAccount class.

import bankaccount

def main():
    # Get the starting balance.
    startBal = float(input("Enter your starting balance: "))

    # Create a BankAccount object.
    savings = bankaccount.BankAccount(startBal)

    # Deposit the user's paycheck.
    pay = float(input("How much were you paid this week? "))
    print("I will deposit that into your account.")
    savings.deposit(pay)

    # Display the balance.
    print(savings)
    
    # Get the amount to withdraw.
    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account.")
    savings.withdraw(cash)

    # Display the balance.
    print(savings)

# Call the main function.
main()