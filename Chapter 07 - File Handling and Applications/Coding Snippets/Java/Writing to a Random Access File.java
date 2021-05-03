/*
Topic Summary
When you write a record to a file that will be used for random
access, you use arithmetic to determine the placement location.

Topic Explanation
Suppose you have products with product numbers and prices. You might want to place records in a random access file so a record can be retrieved on demand without reading through all the records sequentially.

In the Snippet "Creating an Empty File for Random Access", you created a file with 1,000 default records using zeroes for the product numbers and prices. In the program below, when a user enters data for a product, the correct position for the new record is determined by multiplying the product number by the record size. The new data is entered over the default data in the previously empty product file. To keep this example simple, checking for valid product codes and prices was omitted, so when you execute the program, be sure to enter three-digit product codes and five-character prices with a decimal point - for example, 99.99.
*/

import java.nio.file.*;
import java.io.*;
import java.nio.channels.FileChannel;
import java.nio.ByteBuffer;
import static java.nio.file.StandardOpenOption.*;
import java.util.Scanner;
public class CreateProductRandomFile
{
   public static void main(String[] args)
   {
      Scanner input = new Scanner(System.in);
      Path file =
         Paths.get("ProductsForSale.txt");
      String s = "000,00.00" +
         System.getProperty("line.separator");
      final int RECSIZE = s.length();
      FileChannel fc = null;
      String delimiter = ",";
      String numString;
      int num;
      String price;
      final String QUIT = "999";
      try
      {
         fc = (FileChannel)Files.newByteChannel(file, READ, WRITE); 
         System.out.print("Enter product number >> ");
         numString = input.nextLine();
         while(!(numString.equals(QUIT)))
         {
            num = Integer.parseInt(numString);
            System.out.print("Enter price >> ");
            price = input.nextLine();
            s = num + delimiter + price + System.getProperty("line.separator");
            byte[] data = s.getBytes();
            ByteBuffer buffer = ByteBuffer.wrap(data);
            fc.position(num * RECSIZE);
            fc.write(buffer);
            System.out.print("Enter next product number or " + QUIT + " to quit >> ");
            numString = input.nextLine();
         }
         fc.close();
      }
      catch (Exception e)
      {
          System.out.println("Error message: " + e);
      }
   }
}