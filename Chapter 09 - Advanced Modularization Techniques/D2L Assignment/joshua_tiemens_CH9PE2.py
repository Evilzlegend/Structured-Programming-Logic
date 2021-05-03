import random # Imports the needed module for program.


def main():
    
    print()
    display_intro() # Runs the program's proclamation.
    print()

    # Gathers the first user input.
    prob_difficulty = get_prob_difficulty()
    number_one, number_two = display_problem(prob_difficulty)
    
    # Gathers and tests user's answer.
    user_answer = get_answer()
    show_result(user_answer, number_one, number_two)
    
    # Asks to play again.
    again()


# Displays what the program is.
def display_intro():
    print("~~Addition Training~~")

# Get user input for the type of difficulty desired.
def get_prob_difficulty():
    while True:
        try:
            # Initiates the starting input from the user.
            prob_difficulty = int(input("Would you like to add 1 digit, 2 digit, or 3 digit numbers?  "))
            # Displays an error message if user inputs a number outside of parameter.
            while not (prob_difficulty > 0 and prob_difficulty < 4):
                print("Number must be between 1 and 3")
                prob_difficulty = int(input("Would you like to add 1 digit, 2 digit, or 3 digit numbers?  "))
        
        # Displays an error message if the user doesn't enter an integer.
        except:
            print("Number must be an integer")
        
        # Returns the user's difficulty selection to the main().
        else:
            return prob_difficulty

                

# After choice of digit is made, display the problem for end user.
def display_problem(index):
    
    # index 1 runs if user picked 1 digit problems.
    if  index == 1:
        number_one = random.randint(0, 9)
        number_two = random.randint(0, 9)
        print("   ", number_one)
        print("+  ", number_two)
        return number_one, number_two
        
    
    # index 2 run if user picked 2 digit problems.         
    elif index == 2:
        number_one = random.randint(10, 99)
        number_two = random.randint(10, 99)
        print("   ", number_one)
        print("+  ", number_two)
        return number_one, number_two
    
    # else runs if user picked 3 digit problems.        
    else:
        number_one = random.randint(100, 999)
        number_two = random.randint(100, 999)
        print("   ", number_one)
        print("+  ", number_two)
        return number_one, number_two
        

# Program will gather the user's attempted answer.
def get_answer():
    while True:
        try:
            user_answer = int(input("Enter the sum of the numbers: "))
            # Loop error if user inputs invalid keys.
            while not (user_answer >= 0 or user_answer <= 0): 
                print("Value must be a whole number!")
                user_answer = int(input("Enter the sum of the numbers: "))

        except:
            print("Value must be a whole number!")
        # Returns the user's answer to the main() function.
        else:
            return user_answer
        
# Program tests the user's answer if it is correct or wrong.
def show_result(answer_test, num1, num2):
    
    # The sum is calculated through the 'total' variable.
    total = num1 + num2
    
    # Informs the user they were correct and agrees with their answer.
    if answer_test == (total):
        print("You are right! The correct answer is", total, "- Good Work!")
    
    # Informs the user they were wrong and displays correct answer.
    else:
        print("Sorry! You are incorrect... The correct answer is:", total)


# Ask the user if they want to run the program again
def again():
    yesOrNo = input("Do you want to run the program again? ('Y' for yes, anything else to quit)\n")
    
    if yesOrNo.upper() == "Y":
        print()
        main() # Runs the program again from the start.
    
    else: # Ends the program with a farewell message.
        print("Thank you for playing!")
        exit()

main()
