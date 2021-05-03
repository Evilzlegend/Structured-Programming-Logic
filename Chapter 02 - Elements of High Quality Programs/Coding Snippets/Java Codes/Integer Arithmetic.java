# TOPIC SUMMARY
# In Java, you can create arithmetic expressions using any numeric data types.

# TOPIC EXPLANATION
# The addition, subtraction, and multiplication operators are +, -, and * respectively. Addition
# subtraction, and multiplication work as expected, and when you combine data types in an expression,
# the results are the higher-ranking unifying data type. For example, when an int and a double are
# summed, the result is a double.

# Special care must be taken when using the division ( / ) and remainder ( % ) operators with integer
# operands. For example, the value of 16 / 3 is not 5.3333 as you might expect. Instead, it is simply the
# integer portion of the operation, or just 5. If you want to retain the fractional part of an answer after
# integer division, you must cast at least one of the oeprands to a floating-point data type.

# The remainder operator is used to determine the remainder after division, so, for example, 16 % 3 is 1,
# because 3 goes into 16 5 times with a remainder of 1.

# PLAY WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

public class IntegerArithmetic
{
    public static void main(String[] args)
    {
        int itemsMade = 50;
        final int MAX_ITEMS_PER_SHIPMENT = 5;
        int completeShipments = itemsMade / MAX_ITEMS_PER_SHIPMENT;
        int extra = itemsMade % MAX_ITEMS_PER_SHIPMENT;
        double fractionalShipments = (double) itemsMade / MAX_ITEMS_PER_SHIPMENT;
        System.out.println(itemsMade + " items must be sent in " +
            completeShipments + " complete shipments. ");
        System.out.println("That will leave " + extra +
            " extra items which will have to be shipped separately.");
        System.out.println("The shipment is actually " + fractionalShipments +
            " of our standard shipments.");
    }
}
