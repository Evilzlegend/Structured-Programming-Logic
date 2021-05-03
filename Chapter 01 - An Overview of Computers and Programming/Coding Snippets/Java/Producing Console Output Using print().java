/*
TOPIC SUMMARY
The "print()" method produces console output, but unlike "println()", leaves the cursor on the same
line so that subsequent output follows on the same line. You can place the same variety of arguments
within the parentheses of "print()" statemtn as you can with "println()".

TOPIC EXPLANATION
For example:
    - You can use a "String" argument to display a string of characters.
    - You can use a numeric value. You can concatenate combinations of strings and numbers using a
      plus sign.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class PrintDemo
{
    public static void main(String[] args)
    {
        System.out.print("This is a string");
        System.out.print(" with a number on the same line ");
        System.out.print(762);
        System.out.println();
        System.out.print("This is a number " + 512);
        System.out.print(" and another number " + 88 +
            " all on the same line");
    }
}