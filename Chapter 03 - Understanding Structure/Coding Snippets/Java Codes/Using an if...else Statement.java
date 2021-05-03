import java.util.Scanner;
public class IfAndElse
{
   public static void main(String[] args)
   {
      int items;
      double price;
      String msg;
      final double STD_PRICE = 44.66;
      final int HIGH_LIMIT = 12;
      final double LOWER_PRICE = 38.77;
      Scanner input = new Scanner(System.in);
      System.out.print("How many items do you want to order? ");
      items = input.nextInt();      
      if(items >= HIGH_LIMIT)
      {
         price = LOWER_PRICE;
         msg = "You ordered enough for a discount!";
      }
      else
      {
         price = STD_PRICE;
         msg = "If you ordered " + (HIGH_LIMIT - items) +
            " more, you could qualify for a discount.";
      }
      System.out.println(msg);
      System.out.println("Price will be " + price + " each.");
   }
}
