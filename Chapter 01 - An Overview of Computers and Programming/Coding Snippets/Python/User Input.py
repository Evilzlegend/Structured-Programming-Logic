# TOPIC SUMMARY
# The "input" function in Python prompts the user to type something, waits until the user has entered
# the desired text, and returns what the user typed, as a string.

# CODING EXAMPLE:
# The general form for calling the "input" function is below, where the input prompt is an optional
# parameter.
# "input(<prompt string>) ==> <user string>"
# The result of calling "input" is always a string. If we ask the user for a number (or any other non-string
# input), we must convert it to the correct type (see Snippet on "Converting Between Types").

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

yardWidth = float(input("Enter width of yard in feet: "))
yardLength = float(input("Enter length of yard in feet: "))
yardSqFeet = yardWidth * yardLength
# Give each person 15 sq ft, round down
numPeople = int(yardSqFeet / 15.0)

print("Your yard can fit", numPeople, "people")