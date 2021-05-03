# TOPIC SUMMARY:
# The value assigned to a variable may be changed by a new assignment statement. The new value may
# be a modification of the variable's old value, or a completely new value.

# TOPIC EXPLANATION:
# Variables only hold the value assigned to them; they don't remember or reuse the expression that
# generated that value. A variable defined in terms of another variable is not connected to that other
# variable's value.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

x = 125
y = x / 5   # y defined in terms of x
print(x, y)

x = 100     # redefining x
print(x, y)

y = 2 * y   # redefining y by modifying
print(x, y)
