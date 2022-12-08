package se.liu.ida.simja649.tddd78.lab1;

public class Exercise5 {

    public static boolean isPrime(int number) {

        for (int i = 2; i < number; i++) {
            int rest = number % i;
            if (rest == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int min = 2;
        for (int i = min; i < 100; i++) {
            System.out.println(i);
            System.out.println(isPrime(i));
        }
    }
}