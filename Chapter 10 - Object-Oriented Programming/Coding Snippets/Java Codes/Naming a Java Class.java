/*
Topic Summary
Java class names must be one word without embedded spaces, must start with a letter, and can contain letters and numbers, but cannot contain other punctuation. By convention, Java class names start with an uppercase letter. Additionally, Java class names cannot be a Java keyword.

Topic Explanation
All Java programs are contained in a class that you name. Additionally, you might create other classes for your program to use, and you can use prewritten classes such as System and Math that are available in Java.
*/

public class ExplainingPi
{
   public static void main(String[] args)
   {
      System.out.println("Pi represents the ratio between");
      System.out.println("the diameter and circumference"); 
      System.out.println("of a circle");
      System.out.println(Math.PI);
   }
}