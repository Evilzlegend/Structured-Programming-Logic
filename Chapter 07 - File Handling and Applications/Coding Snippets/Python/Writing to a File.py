# TOPIC SUMMARY:
# To open a file for writing, you change the mode specification to 'w' or
# 'a'. The first opens the file for writing, erasing and replacing any
# existing content. The second opens the file for writing, appending any
# new text at the end of the existing content.

# TOPIC EXPLANATION:
# Writing text to a file uses the "write" method. This method takes a single
# string as input, and writes it to the file. You must explicitly include
# newline characters in the output to break it into lines.

# IMPORTANT NOTE: It is essential that the program call the "close" method
# when done writing to the file. The computer tends to be lazy, and only
# writes data to a file when enough has accumulated. If the program does
# not close the file, then some data may not be written to the file when
# the program ends, and it may be lost.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - htere are no limits!

myNovel = open("TheBigMonster.txt", 'w')
text = ['Once upon a time a big monster lives in a forest all alone.',
'The monster had no friends, for no one came near the part of the forest',
'where he lived. He tried to make friends with the forest creatures, but',
'they were frightened by his size and ran away.']

for lineOfText in text:
	myNovel.write(lineOfText + '\n')
myNovel.close()