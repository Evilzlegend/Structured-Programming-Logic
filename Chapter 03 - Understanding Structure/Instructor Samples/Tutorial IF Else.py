#Variables to represent the base hours and
#the overtime multiplier.
baseHours=40  #Base hours per week
otMultiplier=1.5 #Overtime multiplier

#Get the hours worked and the hourly pay rate.
hours=float(input("Enter the number of hours worked: "))
payRate=float(input("Enter the hourly pay rate: "))

#Calculate and display the gross pay.
if hours > baseHours:
    #Calculate the gross pay with overtime.
    #First, get the number of overtime hours worked.
    overtimeHours = hours - baseHours

    #Calculate the amount of overtime pay.
    overtimePay = overtimeHours * payRate * otMultiplier

    #Calculate the gross pay.
    grossPay = baseHours * payRate + overtimePay
else:
    #Calculate the gross pay without overtime.
    grossPay = hours * payRate


    #Display the gross pay.
print("The gross pay is $",format(grossPay,".2f"),sep="")
