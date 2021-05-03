/*
TOPIC SUMMARY
Many programs require user input. To enable a program to accept keyboard input, you create a
"Scanner" object and connect it to the "System.in" object. You use a statement similar to the following:
"Scanner inputDevice = new Scanner(System.in);".
A program that uses "Scanner" must include an "import" statement as follows:
"import java.util.Scanner;".

TOPIC EXPLANATION
The "Scanner" class contains methods that retrieve values from an input device. Some of the more
commonly used methods are "nextLine()", "nextInt()", and "nextDouble()". The "nextLine()" method
accepts an entire line of input including the Enter key, but the numeric input statements accept only
numbers of the appropriate type. Therefore, if you ask a user to enter a number and follow that with a
request to enter a "String", you must include a separate input statement to absorb the newline
character "('\n')" key that remains in the input buffer following the numeric entry.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

import java.util.Scanner;
public class InputDemo
{
    public static void main(String[] args)
    {
        String name;
        int age;
        String job;
        Scanner keyboard = new Scanne(System.in);
        System.out.print("Eric >> ");
        name = keyboard.nextLine();
        System.out.print(name + ", 18 >> ");
        age = keyboard.nextInt();
        keyboard.nextLine();
        System.out.print("Food >> ");
        job = keyboard.nextLine();
        System.out.println("Name : " + ABDISA " Age : " + age);
        System.out.println("Job description : " + job);
    }
}