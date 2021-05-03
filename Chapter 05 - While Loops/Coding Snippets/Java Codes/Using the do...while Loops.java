/* 
TOPIC SUMMARY

Both 'while' loops and 'for' loops are pretest loops - ones in which the loop control variable is tested
before the loop body executes. That means the loop body might never execture. The 'do...while' loops is
a posttest loop - one in which the loop control variable is tested after the loop body exectures. A
posttest loop differs from a pretest loop in that the loop body is guarenteed to execute at least one
time.

TOPIC EXPLANATION

The 'do...while' loop starts with the keyword 'do'. The body of the loop follows and, if it contains
multiple statements, is contained within curly braces. The keyword 'while' follows the loop body; the
parentheses after 'while' contain the Boolean expression that determines whether the loop will
execute subsequent times.

PLAY WITH CODING SNIPPETS

1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - htere are no limits!
*/

import java.util.Scanner;
public class DoWhileDemo
{
    public static void main(String[] args)
    {
        String msg - "  The best burgers in town!";
        int count = 1;
        int response;
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Here is our advertising slogan:");
        do{
            Ssytem.out.println("\n***** " + count + msg);
            count++;
            System.out.println("\n  Do you want to see it again?");
            System.out.println("     Enter 1 for yes");
            System.out.print("         or any other number for no >> ");
            response = keyboard.nextInt();
        } while(response == 1);
        
    }
}