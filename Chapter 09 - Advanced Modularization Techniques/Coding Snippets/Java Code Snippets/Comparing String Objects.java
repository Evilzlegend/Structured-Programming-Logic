/*
Topic Summary

A "String" variable name is a reference; that is, it holds a memory address.
Therefore, if you compare two "String" objects using the equivalency operator (
== ), you are comparing addresses, not the contents of the "String"s. The
"String" class provides a number of useful methods that compare "String"s'
contents.

Topic Explanation

- The "String" class "equals()" method evaluates the contents of two "String"
objects to determine if they are equivalent. The method returns "true" if the
objects have identical contents, or "false" if they do not.

- The "String" class "compareTo()" method compares the contents of "String"s.
It returns 0 if the values of two "String"s are exactly the same, a negative
number if the calling object is 'less than' the argument, or a positive number
if the calling object is 'more than' the argument.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

import java.util.Scanner;
public class ComparingStrings
{
   public static void main(String[] args)
   {
      String word = "dog";
      String guess;
      int compare;
      Scanner input = new Scanner(System.in);
      System.out.println("Try to guess the secret word.");
      System.out.print("It is a three letter word >> ");
      guess = input.nextLine();
      compare = word.compareTo(guess);
      while(!guess.equals(word))
      {
         System.out.print("Sorry. The secret word is ");
         if(compare < 0)
            System.out.print("earlier");
         else
            System.out.print("later");
         System.out.println(" in the alphabet than your word.");
         System.out.print("Try again >> ");
         guess = input.nextLine();
         compare = word.compareTo(guess);
      }
      System.out.println("Yes! The secret word was " + word + "!");
   }
}