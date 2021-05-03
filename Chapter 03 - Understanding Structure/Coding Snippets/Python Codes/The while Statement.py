# TOPIC SUMMARY:
# The "while" loop allows a program to repeat a block of statements for an indefinitely number of time:
# until a Boolean test becomes false.

# CODING EXAMPLE:
# while <test-expression>:
#      <code block>

# Typically the test expression contains one or more variables that are updated in the loop's code block,
# ensuring that the loop does eventually end.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

import random
userNum = int(input("Enter a number between 1 and 10: "))
print("Trying to guess your number...")
myGuess = random.randint(1, 10)
while myGuess != userNum:
    print("I guessed", myGuess, "...trying again")
    myGuess = random.randint(1, 10)
print("I guessed it! Your number was", myGuess)
