# Summary
# In this lab, you work with the same Python program
# you woked with in Labs 5-1 and 5-3. As in those
# earlier labs, the completed program should print
# the numbers 0 through 10, along with their values,
# multiplied by 2 and by 10. However, in this lab you
# should accomplish this using a while loop with
# a break statement.

# Instructions
# 1. Make sure that the file NewestMultiply.py is selected
# and open.
# 2. Write a while loop that uses the loop control variable
# to take on the values 0 through 10 and breaks
# when you loop control exceeds 10.
#3. In the body of the loop, multiply the value of the loop
# control variable by 2 and by 10 and output the result.
# 4. Execute the program by clicking the Run button at the
# bottom of the screen and verify that the output is correct.

head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10:  "
NUM_LOOPS = 10  # Constant used to control loop.
number = 0

print("0 through 10 multiplied by 2 and by 10" + "\n")

# Write while loop
while True:
    print(head1 + str(number))
    print(head2 + str(number * 2))
    print(head3 + str(number * 10))
    number = number + 1
    if number > 10:
        break
