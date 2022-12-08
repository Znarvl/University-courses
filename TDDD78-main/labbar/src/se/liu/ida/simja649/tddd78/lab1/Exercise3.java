package se.liu.ida.simja649.tddd78.lab1;

import javax.swing.*;

public class Exercise3 {


    public static void main(String[] args) {

        int i = 0;
        int sum;

        String input =
                JOptionPane.showInputDialog("Please input a value");
        int tabell = Integer.parseInt(input);
        for (int mult = i; mult <= 12; mult++) {
            sum = mult * tabell;
            System.out.println(mult + " * " + tabell + " = " + sum);

        }

    }
}