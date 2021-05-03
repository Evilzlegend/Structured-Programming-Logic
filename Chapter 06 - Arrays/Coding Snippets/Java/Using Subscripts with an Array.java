/*
TOPIC SUMMARY
Instead of using constant subscript values with array elements, using a variable
subscript makes it much easier to use each element in an array.

TOPIC EXPLANATION
When an application contains an array and you want to use every element of the
array, it is common to perform loops that vary the loop control variable from 0 to
one less than the size of the array. Therefore, it can be convenient to declare a
named constant equal to the size of the array and use it as a limiting value in
every loop that processes the array. As an even better option, you can use the
"length" field that is automatically assigned a value for every array you create. If
you later modify the size of the array and recompile the program, the value in
the "length" field of the array changes appropriately.

 PLAYING WITH CODING SNIPPETS:
 1. Hit the Run button to see the output in the snippet box.
 2. Play around with the snippet code - change variable names, parameters, etc.
 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
 4. Run the correct code again to compare it to the manipulated code.
 5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class UsingVariableSubscripts
{
   public static void main(String[] args)
   {
      int[] codes = {24, 36, 48, 51, 62};
      int x;
      System.out.println("Forwards:");
      for(x = 0; x < codes.length; ++x)
         System.out.print(codes[x] + "   ");
      System.out.println("\nBackwards:");
      for(x = codes.length - 1; x >=0; --x)
         System.out.print(codes[x] + "   ");
   }
}