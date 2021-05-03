#Topic Summary
#The switch statement is useful when you need to test a single
#variable against a series of exact integers (including int, byte,
#and short types), character, or string values.

#Topic Explanation
#The switch statement uses four keywords:
#   switch - starts the statement and is followed immediately by a test
#   expression enclosed in parentheses.

#   case - is followed by one of the possible values for the test expression
#   and a colon.

#   break - optionally terminates a switch statement at the end of each case.
#   Without a break statement after a match, all the statement within the
#   the switch statement execute from that point forward.

#   default - optionally is used prior to any action that should occur if
#   the test variable does not match any case.

#You are never required to use a switch statement; you can always achieve
#the same results with nested if statements. The switch statement is simply
#convenient to use when there are several alternative courses of action
#that depend on a single integer, character, or string value. Most programmers
#would choose to use an if statement if there were only two or three options,
#and to use a switch statement to efficiently manage more discrete options.

import java.util.Scanner;
public class SwitchDemo
{
    public static void main(String[] args)
    {
        String president;
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the name of one of the first four U.S. presidents >> ");
        president = input.nextLine();
        switch(president)
        {
            case "Washington":
                System.out.println("First president!");
                break;
            case "Adams":
                System.out.println("Second president");
                break;
            case "Jefferson":
                System.out.println("Third president");
                break;
            case "Madison":
                System.out.println("Fourth president");
                break;
            default:
                System.out.println("No - not one of the first four");
        }
    }
}
