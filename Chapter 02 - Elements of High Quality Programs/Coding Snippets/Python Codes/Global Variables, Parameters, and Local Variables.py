# TOPIC SUMMARY:
# There are three main kinds of variables in Python: global variables, input parameters for functions, and
# local variables. Each has a distinct purpose and scope. A variable's scope is the part of a program
# where the variable may be used.

# TOPIC EXPLANATION:

# Global variables are defined outside of any function or class, and may be used at any point following
# their definition in the script. They have global scope. Input parameters and local variables both have
# limited scope. Input parameters define the inputs to a function. They are assigned values by a call to
# the function, and their scope is bounded by the function body. Local variables are defined inside
# function definitions. Like parameters, their scope is the function body.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

# Global variables maxVal and minVal
maxVal = 100
minVal = -100

# val is a function parameter
def inBounds(val):
    # Local variables bigEnough and smallEnough
    bigEnough = minVal <= val
    smallEnough = val <= maxVal
    return bigEnough and smallEnough

print(inBounds(55))
print(inBounds(502))
print(minVal, maxVal) # This is okay, global variables are in scope
# print(val)    # This generates an error
# print(bigEnough) # This generates an error