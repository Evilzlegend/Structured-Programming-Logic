# This program displays the records that are
# in the employees.txt file.

# Open the employees.txt file.
empFile = open("employees.txt", 'r')

# Read the first line from the file, which is
# the name field of the first record.
name = empFile.readline()

# If a field was read, continue processing.
while name != '':
    # Read the ID number field.
    idNum = empFile.readline()

    # Read the department field.
    dept = empFile.readline()

    # Strip the newlines from the fields.
    name = name.rstrip("\n")
    idNum = idNum.rstrip("\n")
    dept = dept.rstrip("\n")

    # Display the record.
    print("Name:", name)
    print("ID:", idNum)
    print("Dept:", dept)
    print()

    # Read the name field of the next record.
    name = empFile.readline()

# Close the file.
empFile.close()