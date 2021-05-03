# TOPIC SUMMARY
# Floating-point numbers contain decimal points. The two Java types that hold floating-point numbers
# are double and float.

#TOPIC EXPLANATION
# A double occupies more storage than a float, but a number such as 34.56 is a double by default,
# and you would usually only choose to store it in a float variable if memory limitations were severe. If
# you want to assign a double value to a float, you must follow the value with an F. For example, you
# might make the following declaration: float changeDue = 3.25F;

# You can assign an integer data type to a double, but you cannot assign a double value directly to an
# int. Because of the way floating-point numbers are stored, they can be imprecise.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

public class FloatingPointDemo
{
    public static void main(String[] args)
    {
        double rate1 = 20;
        double rate2 = 80.0;
        double ration = rate1 / rate2;
        float aFloatValue = 5.0F;
        System.out.println("rate 1 :      " + rate1);
        System.out.println("rate 2 :      " + rate2);
        System.out.println("rate 3 :      " + ratio);
        System.out.println("Float value : " + aFloatValue);
    }
}
