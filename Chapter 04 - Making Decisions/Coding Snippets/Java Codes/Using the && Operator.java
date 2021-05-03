import java.util.Scanner;
public class UsingAnd
{
   public static void main(String[] args)
   {
      int yearsOnJob;
      int performanceRating;
      final int YEARS = 2;
      final int RATING = 8;
      Scanner input = new Scanner(System.in);
      System.out.print("How many years has employee been on the job? ");
      yearsOnJob = input.nextInt();      
      System.out.print("What is employee's performance rating? ");
      performanceRating = input.nextInt();  
      if(yearsOnJob >= YEARS && performanceRating >= RATING)
         System.out.println("Bonus is awarded.");
      else
      {
         System.out.println("Not qualified for bonus");
         System.out.println("Must have at least " + YEARS +
            " years on the job and a performance rating of at least " +
            RATING);
      }
   }
}
