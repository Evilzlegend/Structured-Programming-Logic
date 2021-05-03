# TOPIC SUMMARY:
# Once a file is opened for reading, we can get all the text from it in one
# step using the file object's "read" method. This method reads the whole
# file in one step. Once the text is read from a file, it is just a long string,
# and Python's string manipulation tools may be applied to it.

# TOPIC EXPLANATION:
# Note that when a file is opened, the file object keeps track of a cursor in
# the file. The cursor is the location in the text that the program has read
# to. Reading from the file advances the cursor. The "read" method moves
# the cursor all the way to the file's end. Reading at the end of the file
# returns an empty string.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - htere are no limits!

frankenFile = open("Frankenstein.txt", "r")
frankText = frankenFile.read()
nothingLeftText = frankeFile.read()
print(len(frankText), "characters in the text")
if nothingLeftText == "":
    print("Once have read all text, nothing more to read!")
frankenFile.close() # close the file when done