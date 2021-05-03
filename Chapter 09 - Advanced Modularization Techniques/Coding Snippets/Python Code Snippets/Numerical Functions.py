# Topic Summary:

# Python provides a set of useful functions to manipulate numbers. Each function
# is called by listing its name, and then parentheses. Inside the parentheses are
# numbers, separated by commas; the inputs to the function (see Snippet on
# Function Calling for more details).

# Topic Explanation:
# The functions "max" and "min" take a set of numbers and return the largest or
# smallest, respectively. The function "abs" takes the absolute value of a single
# number. The "pow" function is another name for the "**" operator: it takes two
# numbers and returns the result of raising the first number to the power of the
# second number. The "round" function takes one number and rounds it to the 
# nearest integer.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

big = max(55, -29, 102, -300, 76, 15)
small = min(55, -29, 102, -300, 76, 15)
magnitude = abs(small)
print("The range of this data is", big - small)
print("powers of 2:", pow(0, 2), pow(1, 2), pow(2, 2), pow(2, 3))
print("Unrounded:", 70 / 25, "and rounded:", round(70 / 25))