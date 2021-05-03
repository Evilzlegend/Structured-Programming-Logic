/*
TOPIC SUMMARY
An array is a named list of data items that all have the same data type. Each data
item is an element of the array.

CODING EXAMPLE
You declare an array variable by inserting a pair of square brackets after the data
type in the declaration. For example, to declare an array of "int" values to hold
some codes, you can write the following:
"int[] codes;"

After you create an array variable, you still need to reserve memory. You can use
two separate statements as in the following:
"int[] codes;" "codes = new int[5];"

Alternatively, you can declare and create an array in one statement as in the 
following:
"int[] codes = new int[5];"

TOPIC EXPLANATION
You can distinguish each element in an array with a subscript. A subscript is an
integer contained within square brackets that specifies one of an array's
elements. In Java, any array's elements are numbered beginning with 0.
If you use a subscript that is too small (that is, negative) or too large for an array,
the subscript is out of bounds, and an error message is generated.

 PLAYING WITH CODING SNIPPETS:
 1. Hit the Run button to see the output in the snippet box.
 2. Play around with the snippet code - change variable names, parameters, etc.
 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
 4. Run the correct code again to compare it to the manipulated code.
 5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

 public class DeclaringArrays
{
   public static void main(String[] args)
   {
      int[] codes = new int[2];
      double[] sales = new double[10];
      codes[0] = 23;
      codes[1] = 45;
      sales[0] = 34.99;
      sales[9] = 88.33;
      System.out.println("Some codes: " + codes[0] + "  " + codes[1]);
      System.out.println("Some sales: " + sales[0] + "  "  + sales[9]);
   }
}