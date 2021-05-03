# TOPIC SUMMARY:
# Four whole-number data types are available in Java. Each occupies a different amount of memory, and
# each can be positive or negative. The integer types are:

# byte, which occupies one byte and holds values from -128 up to 127.
# short, which occupies two bytes and holds values up to 32,767
# int, which occupies four bytes and holds values up to a little over 2 billion
# long, which occupies eight bytes and holds values with up to 19 digits

# TOPIC EXPLANATION:
# If you use a whole number such as 275 in a Java program, it is the int data type by default. When you
# assign an integer to a byte, short, or int, you do not need to take any special action. To assign a
# value to a long variable, you must add an L to the end of the value. For example, you might make the
# following declaration:
# long nationalDebt = 210000000000L;

# Most whole-number variable in most Java program use the int data type.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

public class IntegerDemo
{
    public static void main(String[] args)
    {
        byte mySiblings = 2;
        int populationMyHomeTown = 12134;
        long populationEarth = 70000000000;
        System.out.println("Siblings: " + mySiblings);
        System.out.println("My town: " + populationMyHomeTown);
        System.out.println("Earth: " + populationEarth);
    }
}
