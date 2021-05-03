/*
Topic Summary
The this reference holds the memory address of the current object that is being used.

Topic Explanation
When you instantiate an object from a class, memory is reserved for each non-static field (that is, instance field) in the class. When you create a method that uses a non-static field value for a class—for example, to get or set the field value—the method must be non-static because it performs in a different way for each object. In Java just one copy of each non-static method in a class is stored, and all instantiated objects can use that method because each non-static method in a class automatically receives a this reference that holds the memory address of the object it references.

Only non-static, instance methods have a this reference. Frequently, you neither want nor need to refer to the this reference within the instance methods that you write, but you can. You must use the this reference when a local variable and a field have the same identifier.
*/

public class ThisDemo
{
   public static void main(String[] args)
   {
      Rug myRug = new Rug("round", 68);
      myRug.display();
   }  
}

// Note: This code should generate an error when run independently.
public class Rug
{
   private String shape;
   private int size;
   public Rug(String shape, int size)
   {
      this.shape = shape;
      this.size = size;
   }
   public void display()
   {
      System.out.println("The rug is " + shape +
         " and is " + size + " inches across.");
   }
}