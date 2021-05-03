# TOPIC SUMMARY:
# Often we want to separate a file into lines and process each line on its
# own. The "readline" and "readlines" methods can be used for this.

# TOPIC EXPLANATION:
# The "readlines" method reads in the entire file, much like "read".
# However, instead of making one big string out of the files's text,
# "readlines" breaks up the lines of the file, and returns a list of strings,
# where each string is a line from the file.

# The "readline" method reads in the entire file, much like "read".
# However, instead of making one big string out of the file's text,
# "readlines" breaks up the lines of the file, and returns a list of strings,
# where each string is a line from the file.

# The "readline" method is finger-grained: it reads in the next line in the file
# advancing the cursor just to the start of the following line.

# Note that both "readline" and "readlines" leave the newline character at
# the end of each line. If you don't want it there, the string "strip" method
# may be used to remove it.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - htere are no limits!

print("------ First pass: readlines")
frankenFile = open("Frankenstein.txt", 'r')
frankLines = frankenFile.readlines()
exerpt = frankLines[1000:1005]
for line in exerpt:
    print(line.strip())
frankenFile.close()
print("------ Second pass: readline")
for i in range(47): # skip first lines
    frankenFile.readline()
keepLines = []
for i in range(10): # store 10 lines
    next = frankenFile.readline()
    keepLines.append(next.strip())
print(keepLines)
frankenFile.close()