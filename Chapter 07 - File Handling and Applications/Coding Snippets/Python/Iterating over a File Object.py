# TOPIC SUMMARY:
# Python can treat a file object as an iterator: you can use a file object in a 
# "for" loop. The result is to loop over the lines of the file, with a similar
# effect to using "readline" or "readlines", but in a more elegant formalism.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - htere are no limits!

frankenFile = open("Frankenstein.txt", 'r')
for line in frankenFile:
    words = line.split()
    if len(words) > 0:
        print(words[0])
frankenFile.close()