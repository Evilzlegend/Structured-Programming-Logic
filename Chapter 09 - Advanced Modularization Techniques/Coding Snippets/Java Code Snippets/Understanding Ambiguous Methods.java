/*
Topic Summary

Overloaded methods are ambiguous when it cannot be determined which
method version should execute.

Topic Explanation

For example, the following methods are ambiguous:
"public static void displayData(String name, int age)"
"public static void displayData(String account, int balance)"

A program with these two methods will not compile because a method call such
as "displayData('Jones', 45):" would be a legal call to either version.

Sometimes, a method is not ambiguous unless a specific type of call is made. For
example, consider these methods:
"public static void displayData(int acctNum, double balance)"
"public static void displayData(double amtOwed, int term)"

A call with an "int" and a "double" argument woudl use the first version, and a call
with a "double" and an "int" would use the second version. However, a call with
two "int" arguments would cause an error because an "int" can be promoted to
a "double", and so the compiler cannot determine which version of the method to
use.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class Ambiguity
{
   public static void main(String[] args)
   {
      double answer1 = 0, answer2 = 0, answer3 = 0;
      answer1 = multiply(4, 6.2);
      answer2 = multiply(5.3, 2);
      // answer3 = multiply(7, 9);
      // The call above is ambiguous
      System.out.println("Answers: " + answer1 +
         "   " + answer2 + "   " + answer3);  
   }
   public static double multiply(int a, double b)
   {
      double answer = a * b;
      return answer;
   }
   public static double multiply(double a, int b)
   {
      double answer = a * b;
      return answer;
   }
}