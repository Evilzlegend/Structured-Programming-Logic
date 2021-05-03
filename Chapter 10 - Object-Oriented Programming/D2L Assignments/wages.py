
# sets the name for the class being created.
class Wages:
    # initializer, collects the three inputs from the user 
    def __init__ (self, name, hours, wage):
        self.__name = name # stores name
        self.__hours = hours # stores hours
        self.__wage = wage # stores wage

    # When called upon, returns the name variable
    def getName(self):
        return self.__name
    # When called upon, displays the printed message with stored variables formatted for presentation.
    def getHours(self):
        print("You entered that", self.__name, "worked {0:,.2f}".format(self.__hours), "hour(s) this week.")
    # When called upon, displays the printed message with stored variables formatted for presentation.    
    def getWage(self):
        print("You entered that", self.__name, "earns ${0:,.2f}".format(self.__wage), "per hour.")


    # defined function to calculate wage based on hours.
    def payForWeek(self):
        if  self.__hours <= 40:
            total = self.__hours*self.__wage # Calculated wage based on 40 or less hours.
            
        elif (self.hours > 40):
            total = ((self.__hours-40)*self.__wage*1.5)+self.__wage*40 # Calculated wage based on regular and overtime pay.
            
        return "${0:,.2f}".format(total) # Returns complete calculated wage with proper formatting.


