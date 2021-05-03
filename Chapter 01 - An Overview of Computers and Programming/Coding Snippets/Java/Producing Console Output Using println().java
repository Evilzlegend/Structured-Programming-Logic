/*
TOPIC SUMMARY
The "println()" method produces a line of console output, leaving the cursor on the next line, ready 
for additional output.

TOPIC EXPLANATION
For example, "System.out.println("Peter Pan");" displays the string 'Peter Pan' and leaves the insertion
point on the next line. "System" is a class, and "out" is an object that represents the default output
device which normally is the monitor. Between the parentheses of "println()", you can place a variety
of arguments.

FOR EXAMPLE:
- You can leave the argument empty, to produce a blank line.
- You can use a "String" argument to display a string of characters.
- You can use a numeric value.
- You can concatenate combinations of strings and numbers using a plus sign.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class PrintlnDemo
{
    public static main(String[] args)
    {
        System.out.println("I");
        System.out.println("want");
        System.out.println("to");
        System.out.println("go");
        System.out.println("to");
        System.out.println("Japan " + 200 +
            " and another number " + 98); 
    }
}