#Explains what the concept of the program is.
print("Enter two integers and I will tell you the relationships they satisfy.")
#Obtain the first integer.
int1=int(input("Enter first integer: "))
#Obtain the second integer.
int2=int(input("Enter second integer: "))
#First if/else statement for equal comparison.
if(int1==int2):
   print(int1, "is equal to",int2)
else:
   print(int1, "is not equal to",int2)
#Second if/else statement for less than comparison.
if(int1<int2):
   print(int1,"is less than",int2)
else:
   print(int1,"is not less than",int2)
#Final if/else statement for lesser or equal to comparison.
if(int1<=int2):
   print(int1,"is less than or equal to",int2)
else:
   print(int1,"is not less than or equal to",int2)

print("Would you like to enter two new numbers?" )
goAgain= input("Enter Y or N ")
while goAgain == "Y":
   print("Enter two integers and I will tell you the relationship they satisfy.")
   #Obtain the first integer.
   int1=int(input("Enter first integer: "))
   #Obtain the second integer.
   int2=int(input("Enter second integer: "))
   #First if/else statement for equal comparison.
   if(int1==int2):
      print(int1, "is equal to",int2)
   else:
      print(int1, "is not equal to",int2)
   #Second if/else statement for less than comparison.
   if(int1<int2):
      print(int1,"is less than",int2)
   else:
      print(int1,"is not less than",int2)
   #Final if/else statement for lesser or equal to comparison.
   if(int1<=int2):
      print(int1,"is less than or equal to",int2)
   else:
      print(int1,"is not less than or equal to",int2)
   print("Would you like to enter two new numbers? ")
   goAgain = input("Enter Y or N ")
if goAgain == "N":
   print("Thank you for playing")

else:
   if goAgain != "Y" or goAgain != "N":
         print("Please enter 'Y' or 'N' ")
      
