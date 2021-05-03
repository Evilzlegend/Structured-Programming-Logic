public class ForDemo
{
    public static void main(String[] args)
    {
        int counter;
        final int LIMIT = 14;
        System.out.println("Counting to " + LIMIT);
        for(counter = 1; counter <= LIMIT; ++counter)
            System.out.print(counter + "  ");
        System.out.println();
    }
}
