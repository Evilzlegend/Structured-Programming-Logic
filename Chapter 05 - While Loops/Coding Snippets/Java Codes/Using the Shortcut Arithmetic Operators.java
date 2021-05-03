public class PrefixPostfixDemo
{
    public static void main(String[] args)
    {
        int myNumber, answer;
        myNumber = 42;
        System.out.println("At start, myNumber is " +
            myNumber);
        answer = ++myNumber;
        System.out.println("After prefix increment, myNumber is " +
            myNumber);
        System.out.println(" and answer is " + answer);
        myNumber = 42;
        System.out.println("Starting over, myNumber is " +
            myNumber);
        answer = myNumber++;
        System.out.println("After postfix increment, myNumber is " +
            myNumber);
        System.out.println(" and answer is " + answer);
