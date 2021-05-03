import coin

# The main function.
def main():
    # Create an object from the Coin class.
    myCoin = coin.Coin()

    # Display the side of the coin that is facing up.
    print("This side is up ", myCoin.get_sideup())

    # Toss the coin.
    print("I am tossing the coin")

    # But now I'm going to cheat! I'm going to
    # directly change the value of the object's
    # sideup attribute to 'Heads'.
    for count in range(10):
        myCoin.toss()
        myCoin.sideup = "Heads"
        print(myCoin.get_sideup())

    # Display the side of the coin that is facing up.
    print("This side is up " , myCoin.get_sideup())

# Call the main function.
main()
