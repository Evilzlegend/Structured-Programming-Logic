# This program calculates a retail item's sale price.

# DISCOUNT_PERCENTAGE is used as a global constant for the discount percentage.
DISCOUNT_PERCENTAGE = 0.20

# The main function.
def main():
    # Get the item's regular price.
    regPrice = get_regular_price()

    # Calculate the sale price.
    salePrice = regPrice - discount(regPrice)

    # Display the sale price.
    print("The sale price is $", format(salePrice, ",.2f"), sep="")

    # Ask user if they want to run the program again.
    again()

# The get_regular_price function prompts the user to enter an item's regular price and it
# returns that value.
def get_regular_price():

    while True:
        try:
            price = float(input("Enter the item's regular price: "))
            while not (price > 0):
                print("Price must be greater than 0.00!")
                price = float(input("Enter the item's regular price: "))
        except:
            print("Value must be an valid price!")
        else:
            break
    return price

# The discount function accepts an item's price as an argument and returns the amount of the
# discount, specified by DISCOUNT_PERCENTAGE.
def discount(price):
    return price * DISCOUNT_PERCENTAGE

# Ask the user if they want to run the program again
def again():
    yesOrNo = input("Do you want to run the program again?) ('Y' for yes, anything else to quit)\n")
    if yesOrNo.upper() == "Y":
        print()
        main()
    else:
        print("FUUUUUUUUUCK YOOOOOOOOOOOOU   :D :D :D")
        exit()

# Call the main function.
main()
