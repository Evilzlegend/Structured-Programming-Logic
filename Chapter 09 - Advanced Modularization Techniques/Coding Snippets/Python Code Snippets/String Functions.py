# Topic Summary:

# The most common built-in function that operates on strings is "len", which
# computes the length of the string, the number of characters in the string.

# The "chr" and "ord" functions convert between integers and their ASCII/Unicode
# equivalent character (a one-symbol string). The "chr" function takes an integer
# and returns the equivalent character, and the "ord" function takes a one-symbol
# string and returns the equivalent integer.
 
# Some other functions can operate on strings, though the results can be odd. For
# instance, the"max" and "min" functions work on strings: they return the symbol
# with the largest or smallest ASCII numberic value.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

s1 = "Mary Poppins"
s2 = "Freddy"
print(len(s1), len(s2))
print(ord('0'), ord('9'), ord('a'), ord('z'))
print(chr(80), chr(97), chr(120))

print(min(s2), max(s2))