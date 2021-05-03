/* 
TOPIC SUMMARY
You call a method by using its name, followed by parentheses ( () ). (If a method requires arguments,
you place them between the parentheses.) A program can call any number of methods any number of
times in any order. Every method can call other methods. A method might return a value, in which case
you can use the method call in the same ways you would use a variable or constant of the same data
type. However methods that use void as a return type do not return any value.

PLAY WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/
public class MethodDemo2
{
    public static void main(String[] args)
    {
        System.out.println("Calling two methods:");
        displayName();
        displayAddress();
        System.out.println("Calling one method");
        System.out.println("    that calls two methods:");
        displayNameAndAddress();
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
    public static void displayNameAndAddress()
    {
        displayName();
        displayAddress();
    }
}
