# TOPIC SUMMARY:
# Sometimes we want our program to perform certain actions if a test is true, and other actions only if
# the test is false. We can add an "else" clause to an "if" statement to get this behavior. The program will
# evaluate the test expression. If it is true, then the code block after the "if" is executed. Otherwise, the
# code block after the "else" is executed.

# CODING EXAMPLE:
# if <test-expression>:
#     <true code block>
# else:
#     <false code block>

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
else:
    print("5x is smaller (or equal)")
if 'tap' in s:
    newS = s.replace('tap', 'TAP')
else:
    newS = s.upper()
print(newS)
