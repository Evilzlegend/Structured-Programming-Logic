public class WhileDemo
{
   public static void main(String[] args)
   {
      int counter;
      final int LIMIT = 24;
      System.out.println("Counting to " + LIMIT);
      counter = 1;
      while(counter <= LIMIT)
      {
         System.out.print(counter + "  ");
         counter = counter + 1;
      }
      System.out.println();
   }
}
