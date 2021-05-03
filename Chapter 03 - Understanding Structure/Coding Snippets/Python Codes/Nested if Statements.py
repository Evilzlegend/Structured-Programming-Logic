# TOPIC SUMMARY:
# Sometimes the answer to one question leads to other questions. "If" statements may appear in the
# code block section of other "if" statements, allowing for a sequence of questions to lead to a specific
# answer.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!


x = 36
y = 12
z = 55
if x <= y:
    if y <= z:
        print("Median is", y)
    elif x <= z:
        print("Median is", z)
    else:
        print("Median is", x)
else:
    if x <= z:
        print("Median is", x)
    elif y <= z:
        print("Median is", z)
    else:
        print("Median is", y)
