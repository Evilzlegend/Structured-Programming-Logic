# Summary
# In this lab the completed program should print the
# numbers 0 through 10, along with their values
# multiplied by 2 and by 10. You should accomplish this
# using a for loop instead of a counter-controlled while loop.

# Instructions
# 1. Write a for loop that uses the loop control variable
# to take on the values 0 through 10.
# 2. In the body of the loop, multiply the value of the 
# loop control variable by 2 and by 10.
# 3. Execute the program and verify that the output is
# correct.

head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10: "

NUM_LOOP_START = 0  # Constant used to control loop
NUM_LOOP_END = 10 # Constant used to control loop

print("0 through 10 multiplied by 2 and by 10.")

# Write your for loop here
for number in range(NUM_LOOP_START, NUM_LOOP_END + 1):
    print(head1 + str(number))
    print(head2 + str(number * 2))
    print(head3 + str(number * 10))