# TOPIC SUMMARY:
# Python 3 provides three operations related to division. The primary division operator, / , always
# produces a floating-point result, and performs normal decimal division.

# The second operator, // , performs integer division, also called the quotient, of two numbers. The
# type of its result matches the type of its operands; if both operands are integers, the result is an int,
# if one or more are floating-point, the result is a float. Any values to the right of the decimal point are
# thrown away.

# The third operator, % , performs the reaminder operation. This goes along with computing the
# quotient: quotitent and remainder is an integer-based way of reporting the result of a division.

# TOPIC EXPLANATION:
# Quotient and remainder together can be a useful way of splitting up numbers into their digits, among
# other applications.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

print("Given 125 people at a dinner, and 8 seats per table...")
people = 125
tableSeats = 8
tablesNeededFloat = people / tableSeats
tablesNeededInt = people // tableSeats
peopleLeftOut = people % tableSeats
print("Decimal tables needed is", tablesNeededFloat)
print("Integer tables needed is", tablesNeededInt)
print("People without table", peopleLeftOut)
print("Splitting", 358, "by digit:", 358 // 10, 358 % 10)
