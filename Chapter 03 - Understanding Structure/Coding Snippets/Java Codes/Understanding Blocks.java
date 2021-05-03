public class BlockDemo
{
   public static void main(String[] args)
   {
      int age = 30;
      System.out.println("Outer:  Age is " + age);
      {
          int weight = 175;
          //int age = 45;
          // statement will not work - age is defined in outer block
          System.out.println("Inner: Age is " + age);
          System.out.println("Inner: Weight is " + weight);
          age = 22;
          System.out.println("Inner after assignment: Age is " + age);
      }
      System.out.println("Outer: Age is " + age);
      // System.out.println("Outer: Weight is " + weight);
      // Statement will not work - weight is out of scope.
   }
}
