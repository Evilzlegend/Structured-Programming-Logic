#Foundation variables used in program
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

#User input for amount of seconds used for conversion.
seconds = int(input("Enter a number of seconds: "))

#First Boolean encounter, ending conversion attempt if statement is false.
if seconds <= 60:
    print("The number of seconds is less than one minute.")

#Second Boolean encounter, applying the correct arithmetic if answer is True
#Otherwise, it'll move on to the next selection.
elif seconds <= 3600:
    print(seconds, "seconds are equal to: ")
    minutes = seconds // seconds_in_minute
    seconds = seconds - (minutes * seconds_in_minute)
    print(minutes, "full minute(s) and", seconds, "seconds.")

#Third Boolean encounter, applying the correct arithmetic like above if answer
#is true, otherwise, it'll move on to the final selection.
elif seconds <= 86400:
    print(seconds, "seconds are equal to: ")
    hours = seconds // seconds_in_hour
    hour_seconds = seconds - (hours*seconds_in_hour)
    minutes = seconds // seconds_in_minute
    minute_seconds = seconds - (minutes*seconds_in_minute)
    seconds = seconds - (hours * seconds_in_hour)
    print(minutes, "full minute(s) and", minute_seconds, "seconds.")
    print(hours, "full hour(s) and", hour_seconds, "seconds.")

#If process reaches this selection, it'll end the program after it applies
#the final arithmetic.
else:
    print(seconds, "seconds are equal to: ")
    days = seconds // seconds_in_day
    hours = seconds // seconds_in_hour
    hour_seconds = seconds - (hours*seconds_in_hour)
    minutes = seconds // seconds_in_minute
    minute_seconds = seconds - (minutes*seconds_in_minute)
    seconds = seconds - (days * seconds_in_day)
    print(minutes, "full minute(s) and", minute_seconds, "seconds.")
    print(hours, "full hour(s) and", hour_seconds, "seconds.")
    print(days, "full day(s) and", seconds, "seconds.")
