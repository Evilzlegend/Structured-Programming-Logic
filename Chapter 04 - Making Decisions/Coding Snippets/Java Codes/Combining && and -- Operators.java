import java.util.Scanner;
public class AndOrDemo
{
    public static void main(String[] args)
    {
        int monParts;
        int tuesParts;
        int wedParts;
        final int GOAL = 200;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number of parts manufactured on:");
        System.out.print("Monday >> ");
        monParts = input.nextInt();
        System.out.print("Tuesday >> ");
        tuesParts = input.nextInt();
        System.out.print("Wednesday >> ");
        wedParts = input.nextInt();
        if(monParts >= GOAL && tuesParts >= GOAL && wedParts >= GOAL)
            System.out.println("We achieved the goal every day");
        else if(monParts >= GOAL && tuesParts >=GOAL || wedParts >= (GOAL * 2))
        {
            System.out.Println("Either we achieved the goal");
            System.out.println("each of the first two days");
            System.out.println("or else we did not BUT");
            System.out.println("we made up for it with at least");
            System.out.println("twiece the goal on Wednesday");
        }
        else System.out.println("Goal not reached");
    }
}
