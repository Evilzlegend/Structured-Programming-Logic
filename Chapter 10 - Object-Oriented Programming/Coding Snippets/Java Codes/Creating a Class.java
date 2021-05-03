/*
Topic Summary
Every Java program is a class; a class that is an application program contains a public static void main() method. You can create other classes from which your application classes instantiate objects. A class is a description or blueprint for objects that will be created from the class.

Topic Explanation
A class header contains three parts:

an access specifier, such as public or private
the keyword class
an identifier; conventionally, a class identifier starts with an uppercase letter
Within a class, you define fields and methods. If every object that is created from a class will have its own data fields, then the fields are not declared to be static. Conventionally, most data fields are private, and most methods are public. Common uses for a class's public methods are to set and retrieve values from the private data fields.
*/

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

