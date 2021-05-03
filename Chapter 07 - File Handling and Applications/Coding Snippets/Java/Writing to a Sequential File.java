/*
TOPIC SUMMARY
A data file can be used as a sequential access file when each record is
accessed one after another in the order in which it was stored.

TOPIC EXPLANATION
For example, you might have a data file of product records that include a
product number, description, and price for each product you sell. Teh
program below reads product data input by a user and writes it to a file
with a comman separating each field. A "BufferedWriter" object uses the
"write()" method to write each record, the "nextLIne()" method to 
separate records so each occupies its own line in the file, and the
"close()" method to close the file when data entry is complete.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - htere are no limits!
*/
import java.nio.file.*;
import java.io.*;
import static java.nio.file.StandardOpenOption.*;
import java.util.Scanner;
public class WriteProductFile
{
   public static void main(String[] args)
   {
      Scanner input = new Scanner(System.in);
      Path file =
         Paths.get("Products.txt");
      String s = "";
      String delimiter = ",";
      int item;
      String description;
      double price;
      final int QUIT = 999;
      try
      {
         OutputStream output = new BufferedOutputStream(Files.newOutputStream(file, CREATE));
         BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output));
         System.out.print("Enter item number >> ");
         item = input.nextInt();
         while(item != QUIT)
         {
            System.out.print("Enter product description >> ");
            input.nextLine();
            description = input.nextLine();
            System.out.print("Enter price >> ");
            price = input.nextDouble();
            s = item + delimiter + description + delimiter + price;
            writer.write(s, 0, s.length());
            writer.newLine();
            System.out.print("Enter next item number or " + QUIT + " to quit >> ");
            item = input.nextInt();
         }
         writer.close();
      }
      catch(Exception e)
      {
         System.out.println("Message: " + e);
      }
   }
}