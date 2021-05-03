/*
Topic Summary
An interface is a description of what a class does, but not how it is done; it declares method headers, but not the instructions within those methods.

Topic Explanation
An interface looks much like a class, except that all of its methods (if any) are implicitly public and abstract, and all of its data items (if any) are implicitly public, static, and final. When you create a class that uses an interface, you include the keyword implements and the interface name in the class header. This notation requires class objects to include code for every method in the interface that has been implemented.
*/
public interface Increasable
{
   public abstract void increase();
}



public class BankAccount implements Increasable
{
   double balance;
   public BankAccount(double bal)
   {
      balance = bal;
   }
   public void increase()
   {
      balance = balance + 1;
   }
   public double getBalance()
   {
      return balance;
   }
}



public class BankAccountDemo
{
   public static void main(String[] args)
   {
      BankAccount acct = new BankAccount(100.25);
      acct.increase();
      System.out.println("New balance: " + acct.getBalance());
   }
}