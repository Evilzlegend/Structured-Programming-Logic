#This program determines whether a bank customer
#qualifies for a loan.

minSalary = 30000.0 #The minimum annual salary
minYears = 2   #The minimum years on the job

#Get the customer's annual salary.
salary = float(input("Enter your annual salary: "))

#Get the number of years on the current job.
yearsOnJob = int(input("Enter the number of " + "years employed: "))

#Determine whether the customer qualifies.
if salary >= minSalary:
    if yearsOnJob >= minYears:
        print("You qualify for the loan.")
    else:
        print("You must have been employed for at least", minYears, \
              "years to qualify.")
else:
    print("You must earn at least $",format(minSalary,'.2f'), "per year to qualify.", sep="")


#Use this combined method to shorten code

#if salary >= minSalary and yearsOnJob >=minYears:
#      print("You qualify for the loan.")
#else:
#       print("You do not qualify for this loan.")
