/*
Topic Summary
You declare an object, also known as an instance of a class, in a statement with the following parts:

the name of the class -- in other words, the data type for the object
an identifier for the object
an assignment operator (=)
the keyword new
a call to the class constructor (a constructor has the same identifier as the class and might require arguments)
You use a public member of a class with an object by using the object's name, a dot, and the method name.
*/

public class ObjectDemo
{
   public static void main(String[] args)
   {
      House myHouse = new House();
      myHouse.setNumBedrooms(3);
      System.out.println("Bedrooms: " +
         myHouse.getNumBedrooms());
   }
}

// Note: This code should generate an error when run independently.
public class House
{
  // the private data members
  private int numBedrooms;
  private double numBaths;
  // the public get and set methods
  public void setNumBedrooms(int number)
  {
	numBedrooms = number;
  }
  public int getNumBedrooms()
  {
	return numBedrooms;
  }
  public void setNumBaths(double baths)
  {
	numBaths = baths;
  }
  public double getNumBaths()
  {
	return numBaths;
  }
}

