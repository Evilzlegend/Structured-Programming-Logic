# TOPIC SUMMARY:
# All functions have names, which follow the same rules as variable names. All function calls have the
# same syntax, shown in general form below. The function call starts with the name of the function. It is followed by a set of parentheses with input values or expressions inside of it, called arguments. Each
# argument is separated from the next by a comma. The number and order of the input values must
# match the function's input parameters.

# CODING EXAMPLE:
# <functionName>(<arg1>, <arg2>, ..., <argn>)

# An argument can be a simple piece of data, or it can be an expression, like an arithmetic expression,
# that evaluates to some value. When the function call is executed , each argument is evaluated, and the
# values are passed to the function.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

print("This is a function call with", 3, "arguments")
x = -251
y = 83
absX = abs(x)
absY = abs(y)
small = min(254 / 3, 2 ** 4, 4 * (12 - 7))
print(absX, absY, small)
fltX = float(x)
print("Type of x is", type(x), "and type of fltX is", type(fltX))
listLen = len([7, 2, 9, 6, 0])
print("List length is", listLen)
