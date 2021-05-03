# This program demonstrates passing two string
# arguments to a function.

def main():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    print("Your name reversed is")
    reverse_name(firstName, lastName)

def reverse_name(first, last):
    print(last, first)

# Call the main function.
main()

