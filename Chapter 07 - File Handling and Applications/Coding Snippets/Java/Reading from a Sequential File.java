/*
TOPIC SUMMARY
When you read records from a sequential file, you read them in order,
starting with the first record.

TOPIC EXPLANATION
The program below reads an example Products.txt file created by the
"WriteProductFile" program in the previous Snippet exercise. The
program declares an "InputStream" for the file, then creates a
"BufferedReader" using the "InputStream". The first line is read into a
"String"; as long as the "readLine()" method does not return "null", the
"String" that contains the fields from the file is displayed, and a new line
is read.

PLAYING WITH CODING SNIPPETS:
1. Hit the Run button to see the output in the snippet box.
2. Play around with the snippet code - change variable names, parameters, etc.
3. Hit the Run button again to see what works and what does not work after you manipulate the code.
4. Run the correct code again to compare it to the manipulated code.
5. Have fun practicing this snppet as many times as you like - there are no limits!
*/

import java.nio.file.*;
import java.io.*;
public class ReadProductFile
{
    public static void main(String[] args)
    {
        Path file =
            Paths.get("Products.txt");
        String s = "";
        try
        {
            InputStream input = new BufferedInputStream(File.newInputStream(file));
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            s = reader.readLine();
            while(s != null)
            {
                System.out.println(s);
                s = reader.readLine();
            }
        }
        catch(Exception e)
        {
            System.out.println("Message: " + e);
        }
    }
}