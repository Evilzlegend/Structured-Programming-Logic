# TOPIC SUMMARY:
# When a Python program encounters an error, it generates an error message called a traceback. Careful
# reading of traceback messages can be helpful in finding and correcting the error.

# CODING EXAMPLE:
# The lines in a traceback show function or method calls that are currently active along with the
# expression where the error actually occurred. Each line lists the filename where the function is defined,
# the line number, the module or function where the function call occurred, and the actual line of code.
# The final line of the traceback describes the error itself.

# Traceback (most recent call last):
#   File "/Users/marta/code/funcExamp.py", line 18, in <module>
#     print(func1(30, 80))
#   File "/Users/marta/code/funcExamp.py", line 9, in func1
#     return func2(a) + func3(b)
#   File "/Users/marta/code/funcExamp.py", line 12, in func2
#     return 2 * func3(100 - x)
#   File "/Users/marta/code/funcExamp.py", line 15, in func3
#     return absx(y - 25)
# NameError: name 'absx' is not defined

# Try uncommenting the code example below on line 2, 3, 4, and 15 to see different traceback
# messages. Then try introducing ner errors to see what the traceback message says.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

# script traceback error:
# x = 3.5
# y = "hello"
# y = x* y

def func1(a, b):
    return func2(a) + func3(b)

def func2(x):
    return 2 * func3(100 - x)

def func3(y):
    return absx(y - 25) # error here!

# print(func1(30, 80))