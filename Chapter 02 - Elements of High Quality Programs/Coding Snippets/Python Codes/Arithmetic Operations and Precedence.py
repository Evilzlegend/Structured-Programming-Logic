# TOPIC SUMMARY:
# The basic arithmetic opeations in Python are similar to other programming languages and close to
# what you learn in math class. Addition uses the + operator, subtraction the - operator.
# Multiplications uses the * operator, and exponentiation is written with the ** operator. There are
# three different operators related to division: / performs floating-point division, // performs integer
# division returning the quotient alone, and % computes the remainder of the division of its operands.

# CODING EXAMPLE:
# Arithmetic expressions may be written with parentheses to make precendence clear, but the built-in
# precendence uses the PEMDAS rule. In order with the highest precedence first, PEMDAS stands for:
# Parentheses, Exponentiation, Multiplication, Division, Addition, Subtraction. As an example, consider
# the following expression:

# 3 + 2 * 4

# Multiplication has a higher precendence than addition, so the computer first computes the
# multiplication, simplifying the expression to 3 + 8, and then it computes the addition: 11.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

a = 10
b = 25
c = 6
print(a + b, a - b, a * b, a / b)
print(b / c, b % c, b ** c)
print(3 * a + b - (c // 2), "equals 52")
print(2 * c ** 2 + c + 2, "equals 80")
