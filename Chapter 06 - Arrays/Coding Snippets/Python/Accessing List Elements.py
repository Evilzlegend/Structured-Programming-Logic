# TOPIC SUMMARY:
# The data in a list may be accessed by its position, its index. Lists are indexed
# starting with 0 at the left end. Just like with strings, negative indices may be used
# to access list elements starting at the right end. The list "[8, 5, 3, 7]" would be
# access like:

# 0 1 2 3
# 8 5 3 7

# -4 -3 -2 -1
#  8  5  3  7

# TOPIC EXPLANATION:
# To access or modify the value, we place square brackets, the access or subscript
# operator, after the likst, with the index inside the brackets. This is often
# pronounced "sub," for instance the expression "mylist[2]" would be pronounced
# as "mylist sub 2."

# If the list subscripting occurs on the left side of an assignment statement, then
# the list is modified to replace the element at that position with the value on the
# right side of the assignment.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

wordList = ['child', 'ball', 'hits', 'buys']
print(wordList[0], wordList[2], wordList[1])
wordList[0] = 'wombat'
print(wordList[0], wordList[2], wordList[1])