# This program demonstrates the in operator
# used with a list.
# item in list

# Create a list of product numbers.
prodNums = ["V475", "F987", "Q143", "R688"]

# Get a product number to search for.
search = input("Enter a product number: ")

# Determine whether the product number is in the list.
if search in prodNums:
    print(search, "was found in the list.")
else:
    print(search, "was not found in the list.")