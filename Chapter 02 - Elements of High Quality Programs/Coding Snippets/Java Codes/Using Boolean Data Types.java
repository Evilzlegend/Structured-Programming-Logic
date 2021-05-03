/*
TOPIC SUMMARY
The "boolean" data type can hold only one of two values: "true" or "false".

TOPIC EXPLANATION
You can assign either of these values to a "boolean" variable, or you can assign the evaluation of a
"boolean" expression. The operators that are used to evaluate "boolean" expressions include "==, >,
<, >=, <=, and !=". The operators that are composed of two characters must not contain a space
between the characters.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

public class BooleanDemo
{
    public static void main(String[] args)
    {
        int myCredits = 35;
        int creditsForSophStatus = 30;
        int creditsToGraduate = 120;
        boolean isEnough = false;
        System.out.println("Initial value: " + isEnough);
        isEnough = myCredits >= creditsForSophStatus;
        System.out.println("Sophomore status: " +
            isEnough);
        isEnough = myCredits >= creditsToGraduate;
        System.out.println("Enough to graduate: " +
            isEnough);
    }
}