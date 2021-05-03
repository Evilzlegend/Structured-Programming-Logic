# TOPIC SUMMARY
# A variable is a named memory location whose contents can change.

#TOPIC EXPLANATION
# In Java, every variable must be declared before it can be used. When you declare a variable, you
# provide the following:
# a data type
# an identifier
# an optional initialization value using an assignment operator (=) and a value
# an ending semicolon

# Java supports eight simple, primitive data types:
# boolean, which holds true or false
# char, which holds a single character such as K or $
# integer (whole number) numeric types which hold value such as 43: byte, short, int, and long
# floating-point (with decimal positions) numeric types which hold values such as 12.7: float and double

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

public class DeclaringVariables
{
    public static void main(String[] args)
    {
        boolean isItANiceDay = true;
        char myGradeInThisClass = 'A';
        int myAge = 35;
        double myPayRate = 167.75;
        System.out.println("It is " + isItANiceDay + " that it is a nice day");
        System.out.println("I expect to get an " + myGradeInThisClass + " in this class")'
        System.out.println("Age is " + myAge + " and pay rate is " + myPayRate);;
    }
}
