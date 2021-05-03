# Summary
# In this lab, you write a while loop that uses a sentinel
# value to control a loop in a Python program. You also
# write the statements that make up the body of the loop.

# The source code file already contains the necessary
# assignment and output statements. Each theater patron
# enters a value from 0 to 4 indicating the number of
# stars that the patron awards to the Guide's featured
# movie of the week. The program executes continously
# until the theater manager enters a negative number to
# quit. At the end of the program, you should display
# the average star rating for the movie.

# Instructions
# 1. Make sure the file MovieGuide.py is seleted and open
# 2. Write the while loop using a sentinel value to control
# the loop, and also write the statements that make up the
# body of the loop.
# 3. Execute the program by cliking the Run button at the
# bottom of the screen.
#   Input the following as star ratings: 0, 3, 4, 4, 1, 1, 2, -1
# Ensure that the average output is correct.

# Initialize variables.


# Initialize variables.
totalStars = 0  # total of star ratings.
numPatrons = 0  # keep track of number of patrons
averageStars = 0 # Average calculated.
numStars = 0 # Number of stars

# Get input.
numStarsString = input("Enter rating for featured movie: ")

# Convert to double.
numStars = float(numStarsString)

# Write while loop here
while numStars >= 0 and numStars <= 4:
    numPatrons = numPatrons + 1 # incrementor
    totalStars = totalStars + numStars
    # Get input.
    numStarsString = input("Enter rating for featured movie: ")


    # Convert to double.
    numStars = float(numStarsString)

# Calculate average star rating
averageStars = totalStars / numPatrons
print("Average Star Value: " + str(averageStars))