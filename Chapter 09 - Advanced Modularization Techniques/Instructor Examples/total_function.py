# This program uses a function to calculate the
# total of the values in a list.

def main():
    # Create a list.
    numbers = [2, 4, 6, 8, 10]

    # Display the total of the list elements.
    print("The total is", get_total(numbers))

# The get_total function accepts a list as an
# argument returns the total of the values in
# the list.
def get_total(valueList):
    # Create a variable to use as an accumulator.
    total = 0

    # Caluclate the total of the list elements.
    for num in valueList:
        total += num

    # Return the total.
    return total

# Call the main function.
main()