/*
Topic Summary

Arrays, like all nonprimitive objects, are reference types. An array's identifier
refers to a memory address where the list of values in the array is stored. When
you pass an array (that is, pass its name) to a method, the receiving method gets
a copy of the array's memory address, which means that the receiving method
has access to, and the ability to alter, the original values in the array.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class PassArray
{
   public static void main(String[] args)
   {
      int[] scores = {76, 82, 90, 75, 92, 88};
      int x;
      System.out.println("Before giving each score a bonus:");
      for(x = 0; x < scores.length; ++x)
         System.out.print(scores[x] + "  ");
      System.out.println();
      giveBonus(scores);
      System.out.println("After giving each score a bonus:");
      for(x = 0; x < scores.length; ++x)
         System.out.print(scores[x] + "  ");
      System.out.println();
   }
   public static void giveBonus(int[] testScores)
   {
      int i;
      final int ADJUSTMENT = 6;
      for(i = 0; i < testScores.length; ++ i)
         testScores[i] += ADJUSTMENT;
   }
}