# TOPIC SUMMARY:
# We build programs out of sets of functions that call each other to perform the program's tasks. The
# first function calls another, which may call another, and so forth. When a function call occurs inside a
# function body, the computer must suspend the first function, remembering where it was in executing
# that function's statements and the values of its variables. It must then start up a new function call, and
# potentially repeat the process.

# TOPIC EXPLANATION:
# The computer uses an internal data structure called a stack to keep track of multiple function calls at
# once. It keeps a stack frame on the stack for each call, where information about the call may be stored.
# Only the function call/frame on top of the stack is active at a given moment in time.

# Python's "traceback" error message will show the stack frames if relevant.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

def funcA(a, b):
    print("Starting funcA")
    print(funcB(a, b))
    print(funcB(b, a))
    print("Ending funcA")

def funcB(x, y):
    print(" In funcB")
    return funcC(x) + y

def funcC(val):
    print("    In funcC")
    return 2 * val

funcA(10, 20)
funcA(15, 16)