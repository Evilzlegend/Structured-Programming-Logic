# Summary
# In this lab, you use a counter-controlled while loop
# in a Python program. When completed, the program should
# print the numbers 0 through 10, along with their values
# multiplied by 2 and by 10. The data file contains the
# nevessary variable declarations and output statements.

# Instructions
# 1. Make sure the file Multiply.py is selected and opened.
# 2. Write a counter-controlled while loop that uses the
# loop control variable (numberCounter) to take on the
# values 0 through 10.
# 3. In the body of the loop, multiply the value of the loop
# control variable by 2 and by 10. Remember to change the
# value of the loop control variable in the body of the loop.
# 4. Execute the program by clicking the Run button at the
# bottom of the screen.

head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10: "
NUM_LOOPS = 10 # Constant used to control loop.

print("0 through 10 multiplied by 2 and by 10" + "\n")

# Initialize loop control variable.
numberCounter = 0
# Write your counter controlled while loop here
while numberCounter <= NUM_LOOPS:
    # Multiply by 10.
    byTen = numberCounter * 10
    # Multiply by 2.
    byTwo = numberCounter * 2
    print(head1 + str(numberCounter))
    print(head2 + str(byTwo))
    print(head3 + str(byTen))
    # Next number
    numberCounter = numberCounter + 1