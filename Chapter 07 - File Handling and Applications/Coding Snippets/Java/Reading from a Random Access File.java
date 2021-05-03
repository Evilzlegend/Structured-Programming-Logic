/*
Topic Summary
With a sequential file, you must read every record in order from the beginning of a file to get to one you need. However, you can access records in any order when you read from a random access file.

Topic Explanation
In the Snippet, "Writing to a Random Access File", a file of product numbers and their prices was created. A record is accessed by multiplying its ID number (which was required to be a three-digit number) by the record size to locate its position in the file.

The file included with this snippet has been populated with example data.
*/

import java.nio.file.*;
import java.io.*;
import java.nio.channels.FileChannel;
import java.nio.ByteBuffer;
import static java.nio.file.StandardOpenOption.*;
import java.util.Scanner;
public class ReadProductsRandomly
{
   public static void main(String[] args)  
   {
      Scanner keyBoard = new Scanner(System.in);
      Path file =
         Paths.get("ProductsForSale.txt");
      String s = "000,00.00" +
         System.getProperty("line.separator");
      final int RECSIZE = s.length();
      byte[] data = s.getBytes();
      ByteBuffer buffer = ByteBuffer.wrap(data);
      FileChannel fc = null;
      String numString;
      int num;
      final String QUIT = "999";
      try
      {
         fc = (FileChannel)Files.newByteChannel(file, READ, WRITE);
         System.out.print("Enter product number or " +
            QUIT + " to quit >> ");
         numString = keyBoard.nextLine();
         while(!numString.equals(QUIT))
         {
            num = Integer.parseInt(numString); 
            buffer = ByteBuffer.wrap(data);
            fc.position(num * RECSIZE);
            fc.read(buffer);
            s = new String(data);
            System.out.println("Product #" + num + "  " + s);
            System.out.print("Enter product number or " +
               QUIT + " to quit >> ");
            numString = keyBoard.nextLine();
         }
         fc.close();
      }
      catch (Exception e)
      {
          System.out.println("Error message: " + e);
      }
   }
}