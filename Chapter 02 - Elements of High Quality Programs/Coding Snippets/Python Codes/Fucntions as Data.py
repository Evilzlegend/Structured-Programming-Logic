# TOPIC SUMMARY:
# In Python, a function definition creates a function object, which is actually a kind of data. The function
# object is assigned to the variable which is its name in the definition. Because functions are actually a
# kind of data, they can be used in the same ways that other kinds of data are: assigned to variables,
# placed in lists, passed as argments, returned as values from functions.

#TOPIC EXPLANATION:
# Using functions as data can be a powerful way to capture abstractions.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

def opToVals(op, valList):
    resList = []
    for val in valList:
        resList.append(op(val))
    return resList

def add1(x):
    return x + 1
def sub1(y):
    return y - 1

def makeAdder(v):
    def adder(x):
        return x + v
    return adder

print(add1, type(add1))
increment = add1
add7 = makeAdder(7)
print(increment(5), sub1(2), add7(10))
opList = [add1, sub1, add7, abs]
for op in opList:
    print(op(25))
print(opToVals(increment, [3, 8, 2, -7]))
