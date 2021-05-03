/*
Using an Array of Objects

Topic Summary
You can declare arrays that hold primitive data types such as int or double, but you also can declare arrays with elements that are objects.

Coding Example
For example, an array named products that holds five Product objects can be defined as:
Product[] products = new Product[5];

You must call the five individual constructors for those objects, using arguments if the constructor requires them. For example, you declare an array of Product objects and name the array products, and if the constructor for the class Product requires an int and a double as arguments, then you might construct one array element as follows:
products[0] = new Product(0, 10.99);
*/
public class ObjectArray
{
   public static void main(String[] args)
   {
      Product[] products = new Product[5];
      int x;
      for(x = 0; x < products.length; ++x)
         products[x] = new Product(x, 10.99);
      for(x = 0; x < products.length; ++x)
         System.out.println(products[x].getItemNum() + "   " + products[x].getPrice());
   }
}

public class Product
{
   private int itemNum;
   private double price;
   Product(int num, double pr)
   {
      itemNum = num;
      price = pr;
   }
   public int getItemNum()
   {
      return itemNum;
   }
   public double getPrice()
   {
      return price;
   }
}