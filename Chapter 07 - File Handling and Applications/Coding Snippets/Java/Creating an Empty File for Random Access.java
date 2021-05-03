/* Topic Summary
A random access file is one for hwich you can access any
record directly without having to go through the records
that come before it sequentially. One approach to creating
a random access file is to start by creating an empty file
that you can add records later.

Topic Explanation
Suppose that you want to create a random access file to
store data about products you sell. Each record includes
a three-digit product number and a five-character price
with decimal place (in the format 99.99). The program
beleow creates an exmpty file to use as a starting point;
it holds 1,000 records, each with product number 000 and
price 00.00. You will use this file as a starting point
when you execute the program in the Snippet "Writing to
a Random Access File". In that program, you will enter a
few records with different product numbers that will
overwrite some of the records in the file created here.

Playing with Coding Snippets:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names,
parameters, etc.
3. Hit the Run button again to see what works and what does
not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snippet as many times as you like - there are no limits!
*/

import java.nio.file.*;
import java.io.*;
import java.nio.ByteBuffer;
import static java.nio.file.StandardOpenOption.*;
public class CreateEmptyProductFile
{
   public static void main(String[] args)
   {
      Path file =
         Paths.get("ProductsForSale.txt");
      String s = "000,00.00" + System.getProperty("line.separator");
      byte[] data = s.getBytes();
      ByteBuffer buffer = ByteBuffer.wrap(data);
      final int NUMRECS = 1000;
      try
      {
         OutputStream output = new BufferedOutputStream(Files.newOutputStream(file, CREATE));
         BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output));
         for(int count = 0; count < NUMRECS; ++count)
             writer.write(s, 0, s.length());
         writer.close();
      }
      catch(Exception e)
      {
          System.out.println("Error message: " + e);
      }
   }
}