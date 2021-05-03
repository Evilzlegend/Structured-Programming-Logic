# This program gets employee data from the user and
# saves it as records in the employee.txt file.

# Get the number of employee records to create.

numEmps = int(input("How many employee records " + \
                        "do you want to create? "))

# Open a file for writing.
empFile = open("employees.txt", 'w')

# Get each employee's data and write it to
# the file.
for count in range(1, numEmps + 1):
    # Get the data for an employee.
    print("Enter data for employee #", count, sep="")
    name = input("Name: ")
    idNum = input("ID number: ")
    dept = input("Department: ")

    # Write the data as a record to the file.
    empFile.write(name + "\n")
    empFile.write(idNum + "\n")
    empFile.write(dept + "\n")

    # Display a blank line.
    print()

# Close the file.
empFile.close()
print("Employee record(s) have been written to employees.txt")