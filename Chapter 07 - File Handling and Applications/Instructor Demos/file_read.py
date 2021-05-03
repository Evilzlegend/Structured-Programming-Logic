# This program reads and displays the content
# of the philosophers.txt file.

# Open a file named philosophers.txt.
infile = open("philosophers.txt", "r")

# Read the file's contents.
fileContents = infile.read()

# Close the file.
infile.close()

# Print the data that was read into
# memory.
print(fileContents)