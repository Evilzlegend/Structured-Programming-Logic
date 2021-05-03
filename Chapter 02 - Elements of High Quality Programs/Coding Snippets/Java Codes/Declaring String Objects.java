# TOPIC SUMMARY
# A literal string is a sequence of characters enclosed within double quotation marks. A literal string
# value can be assigned to a String variable. A String variable is a named object of the String class
# which is defined in java.lang.String, and which is automatically imported into every program you
# write.

# TOPIC EXPLANATION
# When you declare a String object, you can use the class name, an identifier, the keyword new, and
# the String constructor within its parentheses that can contain an initial value. For example:
# String name = new String("Alice");
# Java also provides a shortcut, as in the following:
# String name = "Alice";

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

public class DeclaringStrings
{
    public static void main(String[] args)
    {
        String slogan1 = "I'm lovin' it.";
        String slogan2 = "This is tha bomb diggity"'
        String slogan3 = "this ia fire."'
        System.out.println("Famous advertising slogans:");
        System.out.println(slogan1 + "   **   " + slogan2 +
            "   **   " + slogan3);
    }
}
