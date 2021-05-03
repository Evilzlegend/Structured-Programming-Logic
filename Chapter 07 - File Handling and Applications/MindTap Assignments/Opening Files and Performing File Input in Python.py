# Summary
# In this lab, you open a file and read input from that file in a prewritten Python program. The program should read and print the names of flowers and whether they are grown in shade or sun. The data is stored in the input file named flowers.dat.

# Instructions
# 1. Open source code file named Flowers.py
# 2. Write a while loop to read the input until EOF is reached.
# 3. In the body of the loop, print the name of each flower and where it can be ground (sun or shade).
# 4. Execute the program.

# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input 
# file and prints the information to the user's screen. 
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.
# Open input file
flowFile = open("flowers.dat", "r")
# Write while loop here
flowName = flowFile.readline()
while flowName != "":

    sunShade = flowFile.readline()

    # Strip the newlines
    flowName = flowName.rstrip("\n")
    # Print flower name using the following format
    # print(var + " grows in the " + var2)
    print(flowName, " grows in the ", sunShade)

    flowName = flowFile.readline()

flowFile.close()