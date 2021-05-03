# Topic Summary:
# Programmers create their own functions in order to give a name to a set
# of statements that perform a defined task, and to avoid rewriting the
# same code over and over. To define a function, you must
# (1) give the function a name
# (2) give a variable name for each input to the function, and
# (3) give the statements to be performed when the function is called.
# The syntax of a function definition looks like:

# Coding Example:

# def <functionName>(<param1>, <param2>, ..., <paramN>):
#    """Descriptive comment goes here"""
#     <function body code block>

# When the function is called, each input parameter variable must be
# provided with a value as a part of the call. The function body may refer to
# the parameter variables to access those inputs.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

def printBackwards(text):
    """Takes in a string, and prints it backwards."""
    backwdText = text[::-1]
    print(backwdText)

printBackwards("Hello, World!")
printBackwards("A man, a plan, a canal: Panama!")
printBackwards("Anna Mom Racecar")
