# TOPIC SUMMARY:
# We often update the value of a variable by applying some arithmetic operation to its old value. The
# simplest case of this is incrementing or decrementing the value of a variable. Python provides a special
# assignment operation to make incrementing and shorter to write. Instead of writing x = x + 1 you
# may write x += 1. The increment/decrement amount does not have to be 1, you can increase by any
# value you like.

# TOPIC EXPLANATION:
# There is a version of this shortcut assignment operation for every arithmetic operator. You can update
# a variable by multiplying a value to the old value, by dividing, raising to an exponent, and so forth.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

a = 5
b = 5
print(a, b)

a += 1
b += 2
print(a, b)

c = 2
d = 3
print(c, d)

c *= 5
d **= 2
print(c, d)

d /= 3
print(d)
