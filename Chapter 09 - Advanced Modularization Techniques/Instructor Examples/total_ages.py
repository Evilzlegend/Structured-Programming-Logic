# This program uses the return value of a function.

def main():
    # Get the user's age.
    firstAge = int(input("Enter your age: "))

    # Get the user's best friend's age.
    secondAge = int(input("Enter your best friend's age: "))

    # Get the sume of both ages.
    total = sum(firstAge, secondAge)

    # Display the total age.
    print("Together you are", total, "years old.")

# The sum function accepts two numeric arguments and
# returns the sum of those arguments.
def sum(num1, num2):
    result = num1 + num2
    return result

# Call the main function.
main()
