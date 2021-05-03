# importing the class wages to 
import wages


# defining the main function here.
def main():
    # Disclaimer of what the program does.
    print("The program will create a class storing an employees name and calculates weekly pay for the employee.")
    print()
    # Initializer to start the class engagement.
    userName = input("What is your name? ") # Obtain the user's name.
    userHours = validate_hours() # Obtain the user's hours.
    userWage = validate_wage() # Obtain the user's wage.
    info = wages.Wages(userName, userHours, userWage) # Transfer the user's information to the class's initializer function.
    
    
   # Brings over the attributes from the wages class back to the main()
    (info.getHours()) # hour return
    (info.getWage()) # wage return
    print("Pay for",info.getName(), "is", info.payForWeek()) # Prints returned calculations for user's inputs.
  

    again() # Runs the again function.

    

# defining the validation of hours.
def validate_hours():
    while True:
        hours = input("Enter total hours worked: ") # first attempt to gather input.
        try:
            hours = float(hours)
            if hours > 0: # successful input break out of the while loop.
                break
            else:
                # displays message to remind user the number cannot be negative.
                print("Hours cannot be negative or zero!")
        # ValueError is displayed if user inputs anything other than a number.
        except ValueError:
            print("Hours must be a number!")
    return hours # submits the information once obtained.


# defining the validation of wage.
def validate_wage():
  while True:
    wage = input("Enter your hourly wage: ") # first attempt to gather wage.
    try:
      wage = float(wage)
      if wage > 0: # successful input breaks out of loop.
        break
      else:
          # displays error message to remind user wage cannot be negative.
        print("Wage cannot be negative! ") 
    # ValueErro is displayed if user inputs anything other than a number.
    except ValueError:
      print("Wage must be a number! ")
  return wage   

# defines the again function if user has more entries.
def again():
    yesOrNo = input("Do you want to run the program again? ('Y' for yes, anything else to quit)\n")
    
    if yesOrNo.upper() == "Y":
        print()
        main() # Runs the program again from the start.
    
    else: # Ends the program with a farewell message.
        print("Have a great day!")
        exit()
      
main() # This is where the main() program runs.