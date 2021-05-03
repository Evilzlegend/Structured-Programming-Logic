/*
 TOPIC SUMMARY
 A parallel array is one with the same number of elements as another, and for
 which the values in corresponding elements are related.

 TOPIC EXPLANATION
 For example, you might have an array that holds the names of the 12 months,
 and a corresponding array that holds the number of days that can occur in each
 month. If you find the location of, for example, "May", in the first array, then you
 can access the value 31 from the second, parallel array.

 PLAYING WITH CODING SNIPPETS:
 1. Hit the Run button to see the output in the snippet box.
 2. Play around with the snippet code - change variable names, parameters, etc.
 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
 4. Run the correct code again to compare it to the manipulated code.
 5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

import java.util.*;
public class DaysInMonth
{
   public static void main(String[] args)
   {
      String[] months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
      int[] days = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
      String monthEntered;
      int y;
      Scanner in = new Scanner(System.in);
      System.out.print("Enter a three-letter month name abbreviation >> ");
      monthEntered = in.nextLine();
      for(y = 0; y < months.length; ++y)
         if(months[y].equals(monthEntered))
            System.out.println(months[y] + " can have " + days[y] + " days");
   }
}