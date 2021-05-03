/*
Topic Summary

Overloading a method allows you to use one method identifier to execute
different method versions.

Topic Explanation

If you write multiple methods in the same scope that have the same name, then
they must have different parameter lists. Either the lists must have different
numbers of parameters or the lists. Either the lists must have different
numbers of parameters or the lists must have parameter data types in different
orders. The compiler knows which version of the method to execute based on
the arguments in the method.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class OverloadingMethods
{
   public static void main(String[] args)
   {
      int itemsOrdered = 10;
      double priceEach = 4.75;
      double couponValue = 2.25;
      System.out.print("Case ordered - no discount");
      System.out.println("  " + computePrice(priceEach));
      System.out.print(itemsOrdered + " items ordered - no discount");
      System.out.println("  " + computePrice(itemsOrdered, priceEach));  
      System.out.print(itemsOrdered + " items ordered with coupon");
      System.out.println("  " + computePrice(itemsOrdered, priceEach, couponValue));  
   }
   public static double computePrice(double price)
   {
      final int CASE = 12;
      double total = CASE * price;
      return total;
   }
   public static double computePrice(int items, double price)
   {
      double total = items * price;
      return total;
   }
   public static double computePrice(int items, double price, double discount)
   {
      double total = items * price - discount;
      return total;
   }
}