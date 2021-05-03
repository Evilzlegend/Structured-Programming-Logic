/*
Topic Summary
In Java, a method is an encapsulated section of code that can be invoked
from another method. Every method contains a header and a body.

Topic Explanation
A method's header consists of the following:
- an access specifier such as "public" or "private"
- the keyword "static" if the method will be called without using an
  object
- a return type, which can be any data type or "void" if the method does
  not return a value. 
- a method name, which can be any legal identifier
- a pair of parentheses (()) that can contain a parameter list if data
  should be passed into the method.

The body of a method is written between a pair of curly braces ({}) and
can contain any number of statements including variable declarations and
calls to other methods.

You can place methods in any order in a program. A program's "main()"
method executes first no matter where it is placed in a file.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/
public class MethodDemo
{
    public static void main(String[] args)
    {
        displayName();
        displayAddress();
    }
    public static void displayName()
    {
        System.out.println("Johnathan Livingston");
    }
    public static void displayAddress()
    {
        System.out.println("345 Seafarer Way");
        System.out.println("Punta Gorda, FL 33950");
    }
}