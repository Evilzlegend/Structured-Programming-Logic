# Initialize a sentinel
quit = "Y"

# Create the loop
while quit == "Y":

    print("You enter a dark room with two doors.")
    print("Do you go through door #1 or door #2?")
    choice=int(input(" "))
    if(choice==1):
        print("There's a giant bear here eating a cheese cake.")
        print("What do you do?")
        print("1. Take the cake.")
        print("2. Scream at the bear.")
        choice=int(input(" "))
        if(choice==1):
            print("The bear mauls you to death.")
            print("")
            print("Do you want to play again?")
            # Check for Sentinel
            quit = input("Enter Y or N: ")
        elif(choice==2):
            print("The bear eats your legs off.")
            print("")
            print("Do you want to play again?")
            # Check for Sentinel
            quit = input("Enter Y or N: ")
        else:
            print("You wait until the bear leaves before continuing on.")
            print("")
            print("Do you want to play again?")
            # Check for Sentinel
            quit = input("Enter Y or N: ")
    elif(choice==2):
        print("There's a sleeping cat sitting by the fireplace.")
        print("What do you do?")
        print("1. Throw a fish.")
        print("2. Put out the fire.")
        choice=int(input(" "))
        if(choice==1):
            print("The cat wakes up and eats the fish, leaving you alone.")
            print("")
            print("Do you want to play again?")
            # Check for Sentinel
            quit = input("Enter Y or N: ")
        elif(choice==2):
            print("The cat wakes up and claws off your face.")
            print("")
            print("Do you want to play again?")
            # Check for Sentinel
            quit = input("Enter Y or N: ")
        else:
            print("You ignore the cat and move on.")
            print("")
            print("Do you want to play again?")
            # Check for Sentinel
            quit = input("Enter Y or N: ")
    else:
        print("You sit in the room for the rest of time, paralyzed with indecision.")
        print("")
        print("Do you want to play again?")
        # Check for Sentinel
        quit = input("Enter Y or N: ")