# TOPIC SUMMARY:
# Our programs need to be able to choose when to perform certain steps. The "if" statement allows the
# program to ask a question about data and only executes a block of statements if the question is true.

# CODING EXAMPLE:
# The "if" statement starts with the keyword "if", followed by an expression that evaluates to true or
# false, and then a colon. The block to be executed is indented starting on the next line.

# if <test-expression>:
#   <code block>

# Note: "True" and "False" are Python Boolean values, but Python allows expressions that evaluate to
# other values in the test expression. Other values (numbers, strings, lists) are considered true except
# for: "None", zero in any numeric form, empty sequences("", [], etc.), and empty sets/dictionaries.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

s = 'catapult'
x = 25
z = 123
if 5*x > z:
    print("5x is bigger")
if 'tap' in s:
    print(s, "contains tap")
