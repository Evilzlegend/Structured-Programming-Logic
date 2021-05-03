public class NestedLoopDemo
{
    public static void main(String[] args)
    {
        int outer;
        int inner;
        final int OUTER_LIMIT = 5;
        final int INNER_LIMIT = 10;
        for(outer = 0; outer < OUTER_LIMIT; ++outer)
        {
            System.out.print("Outer " + outer + "    ");
            for(inner = 0; inner < INNER_LIMIT; ++inner)
                 System.out.print(inner + "  ")
            System.out.println();
        }
    }
}

