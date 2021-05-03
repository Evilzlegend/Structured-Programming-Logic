# Create sentinel value
quit = "Y"

# Start of Loop
while quit == "Y":
   # Ask for user input
   print("Enter two integers and I will tell you the relationships they satisfy.")
   int1=int(input("Enter first integer: "))
   int2=int(input("Enter second integer: "))

   # Equal Determination
   if(int1==int2):
      print(int1,"is equal to",int2)
   else:
      print(int1, "is not equal to",int2)

   # Less than Determination
   if(int1<int2):
      print(int1, "is less than",int2)
   else:
      print(int1, "is not less than",int2)

   # Less than or equal to Determination
   if(int1<=int2):
      print(int1,"is less than or equal to",int2)
   else:
      print(int1,"is not less than or equal to",int2)
   
   # Print output
   print("")
   print("Do you want to enter two more numbers?")

   # Check for Sentinel
   quit = input("Enter Y or N: ")
   if quit == "N":
      print("Have a great day!")