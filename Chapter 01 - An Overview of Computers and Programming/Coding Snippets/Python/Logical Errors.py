# TOPIC SUMMARY
# The hardest errors to find and remove from a program are logical errors. These errors do not cause
# the program to crash and generate a traceback message. Instead, a logical error means an error in the
# programmer's thinking: the program runs, but produces the wrong answer.

# Find and correct the logical error in every code fragment.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

# If first and last elements of a list are equal, print "YES"
lst = [93, 21, 75, 87, 93]
lstLen = len(lst)
if lst[1] == lst[lstlen-1]:
    print("YES")
else:
    print("NO")

# Convert inches to feet
numInches = 256.25
numFeet = numInches / 12
print("Inches =", numInches, "Feet =", numFeet)

# Count vowels in a string
text = "We are such stuff as dreams are made on; and our little life is rounded with a sleep."
count = 0
for ch in text:
    if ch == 'a' or 'e' or 'i' or 'o' or 'u':
        count += 1
print("Vowel count =", count)