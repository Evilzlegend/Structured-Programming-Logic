/*
Topic Summary

A called method can return a value to the method that called it. The returned
value can be any data type. The data type of the value returned must match the 
return type listed in the method's header (or must be able to be automatically
promoted to that type). If a method does not return any value, then its return
type is "void".

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/
public class ReturningValues
{
   public static void main(String[] args)
   {
      int measurement = 5;
      int area = getArea(measurement);
      int volume = getVolume(measurement);
      System.out.println("A square with a side of " +
         measurement + " has an area of " + area);
      System.out.println("A cube with a side of " +
         measurement + " has a volume of " + volume);
   }
   public static int getArea(int side)
   {
      int area = side * side;
      return area;
   }
   public static int getVolume(int side)
   {
      int volume = side * side * side;
      return volume;
   }
}