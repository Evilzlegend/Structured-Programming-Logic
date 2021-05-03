# TOPIC SUMMARY
# Python errors have an error type associated with them. Along with careful reading of the actual error
# message, the error type can give us an idea of what caused the error. Some common error types are
# "SyntaxError", "IdentationError", "NameError", "TypeError", "ImportError", "IndexError", and "KeyError".

# The table below describes each error type and common causes.

# TOPIC EXPLANATION
# Error type        Description
# SyntaxError       The program contains "ungrammatical" Python, often missing quotes or parentheses
# IndentationError  An indented block of code is expected, but none is found.
# NameError         A name (typically or a variable, function, or method) is not recognized, most often due to a spelling error
# TypeError         An operation is given data of the wrong type
# ImportError       A module cannot be found or imported, often because of a misspelling of the module name, or misplacement of the module
# IndexError        A subscript operator accesses a sequence with an index is out of range
# KeyError          A subscript operator accesses a dictionary with a key that is not in it

# The examples below illustrate each of these types of errors. To generate each error, uncomment the
# code for that error and click Run.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

x = 30
s = "hello"

# if x > 20         # SyntaxError
#     print("big")

# if x > 20:        # IndentationError
# print("Big")

# if x > y:         # NameError
#     print(x)

# z = 2.7 * s       # TypeError

# import maths      # ImportError

# lst = ['robin', 'sparrow', 'hummingbird']  # IndexError
# print(lst[3])

# table = {'robin': 25, 'sparrow': 130, 'hummingbird': 5}   #KeyError
# print(table['robin'], table['duck'])