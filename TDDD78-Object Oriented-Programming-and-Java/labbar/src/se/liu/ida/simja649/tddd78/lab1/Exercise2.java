package se.liu.ida.simja649.tddd78.lab1;

import javax.swing.*;

public class Exercise2 {


    private static void sumFor(int min, int max) {
        int sum = 0;
        for (int i = min; i <= max; i++) {


            sum += i;
            System.out.println(sum);

        }

    }

    private static void sumWhile(int min, int max) {
        int i = min;
        int sum = 0;
        while (i <= max) {

            sum += i++;

            System.out.println(sum);

        }

    }

    public static void main(String[] args) {
        int min = 10;
        int max = 20;

        String input =
                JOptionPane.showInputDialog("Please input a value");
        switch (input) {
            case "for":
                System.out.println("for loop");
                sumFor(min, max);
                break;
            case "while":
                System.out.println("while loop");
                sumWhile(min, max);
                break;
            default:
                System.out.println("Not valid response");
        }



    }
}



