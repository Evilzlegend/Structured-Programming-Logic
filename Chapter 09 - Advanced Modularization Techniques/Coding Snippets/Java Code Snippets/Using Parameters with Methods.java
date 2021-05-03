/*
Topic Summary

Sometimes you need to send data to a method. When a method must receive a
parameter, you include a data type and identifier between the parentheses in the
method header. (If there are multiple parameters, you create a comma-
separated list.)

Topic Explanation

When you call a method that receives a parameter, you include an item, called an
argument, between the parentheses in the method call. The argument to a
method must be the same data type as the method's parameter. The argument
to a method can be a variable or a constant; it also could be the result of an
arithmetic expression or the value returned from another method. (If a method
accepts multiple parameters, the arguments must be in the correct order.)

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/
public class DemoTaxMethod
{
    public static void main(String[] args)
    {
        double price1 = 13.82;
        double price2 = 21.53;
        displayTax(price1);
        displayTax(price2);
        displayTax(200.00);
    }
    public static void displayTax(double price)
    {
        final double RATE = 0.09;
        double tax;
        tax = price * RATE;
        System.out.println("The tax on $" +
            price + " is $" + tax);)
    }
}