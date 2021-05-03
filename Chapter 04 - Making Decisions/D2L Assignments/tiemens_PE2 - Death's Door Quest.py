#Begin the quest entering the room with two doors.
print("You enter a dark room with two doors.")
#Prompting the first decision for the user.
print("Do you go through door #1 or door #2?")
#First choice user prompt.
choice=int(input(" "))
#Outcome of first choice user prompt.
if(choice==1):
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    choice=int(input(" "))
    if(choice==1):
        print("The bear mauls you to death.", end=" ")
    elif(choice==2):
        print("The bear eats your legs off.", end=" ")
    else:
        print("You wait until the bear leave before continuing on.", end=" ")
#If user picked choice 2, this will be the outcome module.
elif(choice==2):
    print("There's a sleeping cat sitting by the fireplace.")
    print("What do you do?")
    print("1. Throw a fish.")
    print("2. Put out the fire.")
    choice=int(input(" "))
    if(choice==1):
        print("The cat wakes up and eats the fish, leaving you alone.", end=" ")
    elif(choice==2):
        print("The cat wakes up and claws off your face.", end=" ")
    else:
        print("You ignore the cat and move on.", end=" ")
#If user initially picks anything other than 1 or 2 the program will immaturely end.
else:
    print("You sit in the room for the rest of time, paralyzed with indecision.", end=" ")

    print("Good job!")
