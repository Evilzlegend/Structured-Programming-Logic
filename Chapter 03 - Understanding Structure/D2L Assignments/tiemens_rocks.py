# Variables to use for user.
tiny = 1
small = 6
medium = 12
large = 18
twelveStone = 168

#User input for tiny rocks.
tinyRock = int(input("How many tiny rocks were used? "))
#Calculate the tiny rock total weight.
tinyRockTotal = tinyRock*tiny
#Print the total of tiny rocks.
print("Your total weight for tiny rocks is: ", (format(tinyRockTotal, '.2f')), "pounds.")


#User input for small rocks.
smallRock = int(input("How many small rocks were used? "))
#Calculate the small rock total weight.
smallRockTotal = smallRock*small
#Print the total of small rocks.
print("Your total weight for small rocks is: ", (format(smallRockTotal, '.2f')),"pounds.")


#User input for medium rocks.
mediumRock = int(input("How many medium rocks were used? "))
#Calculate the medium rock total weight.
mediumRockTotal = mediumRock*medium
#Print the total of medium rocks.
print("Your total weight for medium rocks is: ", (format(mediumRockTotal, '.2f')), "pounds.")


#User input for large rocks.
largeRock = int(input("How many large rocks were used? "))
#Calculate the large rock total weight.
largeRockTotal = largeRock*large
#Print the total of large rocks.
print("Your total weight for large rocks is: ", (format(largeRockTotal, '.2f')), "pounds.")


#Calculate total of all rocks.
total = largeRockTotal+mediumRockTotal+smallRockTotal+tinyRockTotal
#Print the total of all rocks.
print("You have a total of, ", (format(total, '.2f')), "pounds of rock.")


#Else-if formula for 12 stone configuration
if total == twelveStone:
    print("You have 12 stone.")
elif total > twelveStone:
    print("You have more than 12 stone.")
elif total < twelveStone:
    print("You have less than 12 stone.")
