import java.util.Scanner;
public class SingleAlternativeIfs
{
   public static void main(String[] args)
   {
      int items;
      double price;
      final double STD_PRICE = 11.22;
      final int LOW_LIMIT = 4;
      final double HIGHER_PRICE = 12.45;
      final int HIGH_LIMIT = 12;
      final double LOWER_PRICE = 9.77;
      Scanner input = new Scanner(System.in);
      System.out.print("How many items do you want to order? ");
      items = input.nextInt();      
      price = STD_PRICE;
      if(items < LOW_LIMIT)
         price = HIGHER_PRICE;
      if(items > HIGH_LIMIT)
         price = LOWER_PRICE;
      System.out.println("Price will be " + price + " each.");
   }
}
