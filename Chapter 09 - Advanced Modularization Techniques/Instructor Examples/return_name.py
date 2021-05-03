def main():

    firstName, lastName = get_name()
    print(firstName, lastName)

def get_name():
    # Get the user's first and last names.
    first = input('Enter your first name: ')
    last = input("Enter your last name: ")
    # Return both names.
    return first, last

main()
