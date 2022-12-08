package se.liu.ida.simja649.tddd78.lab1;

import javax.swing.*;

public class Exercise9
{
    public static double findRoot(double x) {
	double guess = x;
	for (int i = 0; i <= 10; i++) {
	    guess = guess - (guess * guess - x) / (2 * guess);

	}
	return guess;

    }

    public static void main(String[] args) {
	String x = JOptionPane.showInputDialog("Please input a value");
	double value = Double.parseDouble(x);

	System.out.println(findRoot(value));

    }
}
