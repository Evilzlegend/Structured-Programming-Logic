# Topic Summary:

# Many built-in functions return value, inluding "len", "max", and"abs". When
# called, they are passed inputs, and they produce a resulting value. To define a
# function that returns a value, we use the special command "return" which may
# be followed by zero, one, or more values. When the program reaches the
# "return" statement, the function execution ceases immediately and the values
# are returned.

# Topic Explanation:

# The values returned by a function call may be used by the program if it sets a
# variable to hold the result, or uses the function call in an expression or
# statement.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

def absDiff(num1, num2):
    """Takes in two numbers and returns the absolute value of the
    difference between the numbers."""
    diff = num1 - num2
    return abs(diff)

val1 = absDiff(35, 72)
val2 = absDiff(10, 4)
print(val1, val2, absDiff(3, -2), 2 * absDiff(66, 77))