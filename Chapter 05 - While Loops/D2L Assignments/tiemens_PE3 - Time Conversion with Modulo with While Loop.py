#Local variables
days = 0
hours = 0
minutes = 0
seconds = 0
dayRemainder = 0
hourRemainder = 0
minuteRemainder = 0

#Get the number of seconds from the user.
seconds = int(input('Enter the number of seconds: '))

# Calculate the number of days.
if seconds >= 86400:
    days = seconds // 86400
    dayRemainder = seconds % 86400
    
# Calculate the hours.
if seconds >= 3600:
    hours = seconds // 3600
    hourRemainder = seconds % 3600

# Calculate the minutes.
if seconds >= 60:
    minutes = seconds // 60
    minuteRemainder = seconds % 60

# Display days, hours, minutes, seconds.
if minutes == 0:
    print('The number of seconds is less than one minute.')
else:
    print(seconds, 'seconds are equal to:')
    print (minutes, 'full minute(s) and', minuteRemainder, 'seconds.')
    if hours!=0:
        print (hours, 'full hour(s) and', hourRemainder, 'seconds.')
    if days!=0:
        print (days, 'full day(s) and', dayRemainder, 'seconds.')

print("Would you like to enter a new set of numbers?")
goAgain=input("Enter Y or N ")
while goAgain == "Y":
    seconds = int(input('Enter the number of seconds: '))

    # Calculate the number of days.
    if seconds >= 86400:
        days = seconds // 86400
        dayRemainder = seconds % 86400
    
    # Calculate the hours.
    if seconds >= 3600:
        hours = seconds // 3600
        hourRemainder = seconds % 3600

    # Calculate the minutes.
    if seconds >= 60:
        minutes = seconds // 60
        minuteRemainder = seconds % 60

# Display days, hours, minutes, seconds.
    if minutes == 0:
        print('The number of seconds is less than one minute.')
    else:
        print(seconds, 'seconds are equal to:')
        print (minutes, 'full minute(s) and', minuteRemainder, 'seconds.')
        if hours!=0:
            print (hours, 'full hour(s) and', hourRemainder, 'seconds.')
        if days!=0:
            print (days, 'full day(s) and', dayRemainder, 'seconds.')
        print("Would you like to enter a new set of time?")
        goAgain = input("Enter Y or N ")
# Stops program if user decides to not enter new seconds.
if goAgain == "N":
    print("Good bye.")
# While loop to cover user not pressing the correct key.
else:
    if goAgain != "Y" or goAgain != "N":
        print("Please enter 'Y' or 'N' ")
        goAgain = input("Enter Y or N ")
        while goAgain == "Y":
            seconds = int(input('Enter the number of seconds: '))
            if seconds >= 86400:
                days = seconds // 86400
                dayRemainder = seconds % 86400

            if seconds >= 3600:
                hours = seconds // 3600
                hourRemainder = seconds % 3600

            if seconds >= 60:
                minutes = seconds // 60
                minuteRemainder = seconds % 60

            if minutes == 0:
                print("The number of seconds is less than one minute.")
            else:
                print(seconds, "seconds are equal to:")
                print(minutes, "full minute(s) and", minuteRemainder, "seconds.")
            if hours !=0:
                print (hours, "full hour(s) and", hourRemainder, "seconds.")
            if days != 0:
                print(days, "full day(s) and", dayRemainder, "seconds.")
            print("Would you like to enter a new set of time?")
            goAgain = input ("Enter Y or N ")
        else:
            if goAgain == "N":
                print("Have a great day!")
