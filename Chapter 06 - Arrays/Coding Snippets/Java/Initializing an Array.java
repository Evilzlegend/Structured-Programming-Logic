/*
TOPIC SUMMARY
Array names contain references. No memory address is assigned when you
declare an array using only a data type, brackets, and a name. Instead, the array
variable name has the value "null", which means the identifier is not associated
with a memory address. You must take further action to assign a memory
address to an array name and values to array elements.

TOPIC EXPLANATION
When you use the keyword "new" to define an array, the array reference acquires
a memory address value, and each element acquires a default value. Numeric
array elements are assigned 0, "char" and "object" array elements are assigned
"null", and "boolean" array elements are assigned "false".

You can also assign nondefault values to array elements upon creation using an
initialization list of values separated by commas and enclosed within curly
braces. When you populate an array upon creation by providing an initialization
list, you do not give the array a size-the size is assigned based on the number of
values you place in the initializing list. In Java, you cannot directly initialize part of
an array. For example, you cannot create an array of eight elements and initialize
only four; you either must initialize every element or none of them.

 PLAYING WITH CODING SNIPPETS:
 1. Hit the Run button to see the output in the snippet box.
 2. Play around with the snippet code - change variable names, parameters, etc.
 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
 4. Run the correct code again to compare it to the manipulated code.
 5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class InitializingArrays
{
   public static void main(String[] args)
   {
      int[] codes = {24, 36, 48, 51, 62};
      double[] sales = new double[10];
      System.out.println("Some codes: " + codes[0] + "  " + codes[1]);
      System.out.println("Some sales: " + sales[0] + "  "  + sales[9]);
   }
}