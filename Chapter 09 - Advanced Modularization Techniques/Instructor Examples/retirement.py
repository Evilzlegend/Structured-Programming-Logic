# The following is used as a global constant to represent
# the contribution rate.
CONTRIBUTION_RATE = 0.05  # All caps to show it's a non-changing variable.

def main():
    grossPay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses: "))
    show_pay_contrib(grossPay)
    show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross
# pay as an argument and displays the retirement
# contribution for that amount of pay.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(contrib, ",.2f"), sep="")

# The show_bonus_contrib functon accepts the
# bonus amount as argument and displays the
# retirement contribution for that amount of pay.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print("Contribution for bonuses: $", format(contrib, ",.2f"), sep="")

# Call the main function.
main()
