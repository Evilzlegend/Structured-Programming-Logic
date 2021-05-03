# SUMMARY

# In this lab, you use what you have learned about searching a list to find an exact
# match to complete a partially prewritten Python program.

# The program uses a list that contains valid names for 10 cities in Michigan. You 
# ask the user to enter a city name; your program then searches the list for that city
# name. If it is not found, the program should print a message that informs the user 
# the city name is not found in the list of valid cities in Michigan.

# The starter file provided for this lab includes input statements. You need to write
# code to examine all the items in the list and test for a match. You also need to 
# determine if you should print the "Not a city in Michigan." message. Comments in
# the code tell you where to write your statements.

# INSTRUCTIONS
# 1. Study the prewritten code to make sure you understand it.
# 2. Write a loop statement that examines the names of cities stored in the list.
# 3. Write code that tests for a match.
# 4. Write code that, when appropriate, prints the message "Not a city in Michigan".
# 5. Execute the program using the following as input:
#   Chicago, Brooklyn, Watervliet, Acme

# MichiganCities.py - This program prints a message for invalid cities in Michigan.
# Input:  Interactive
# Output: Error message or nothing

# Initialized list of cities:
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet", "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"]

# Get user input
inCity = input("Enter name of city: ")

# Write your test statement here to see if there is a match.
for i in range(len(citiesInMichigan)):
    if citiesInMichigan[i] == inCity:
        test = True
        break
    else:
        test = False
if test:
    print("City found.")
else:
    print("Not a city in Michigan.")
# If the city is found, print "City found."

# Otherwise, "Not a city in Michigan" message should be printed.