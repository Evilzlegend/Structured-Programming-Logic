# This program converts cups to fluid ounces.
def main():
    # display the intro screen.
    intro()

    # Get the number of cups.
    while True:
        try:
            cupsNeeded = int(input("Enter the number of cups: "))
        except:
            print("Value must be an integer")
        else:
            break
    
    # Convert the cups to ounces.
    cups_to_ounces(cupsNeeded)
    again()

# The intro function displays an introductory screen.
def intro():
    print()
    print("This program converts mesasurement from cups to fluid ounces")
    print("1 cup = 8 fluid ounces")
    print()
# The cups_to_ounces function accepts a number of
# cups and displays the equivalent number of ounces.
def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")

def again():
    yesorNo = input("Do you want to run the program again? ('Y' for yes, anything else to quit)\n")
    if yesorNo.upper() == "Y":
        print()
        main()
    else:
        print("Good bye!")
        exit()


# Call the main function.
main()
