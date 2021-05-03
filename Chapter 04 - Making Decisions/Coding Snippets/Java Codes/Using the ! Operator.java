import java.util.Scanner;
public class NotDemo
{
    public static void main(String[] args)
    {
        int credits;
        final int FULLTIME = 15;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the credits in which");
        System.out.print("    you are enrolled this semester >> ");
        credits = input.nextInt();
        if(!(credits >= FULLTIME))
            System.out.println("You are not a fulltime student.");
        else System.out.println("You are a fulltime student.");
    }
}
