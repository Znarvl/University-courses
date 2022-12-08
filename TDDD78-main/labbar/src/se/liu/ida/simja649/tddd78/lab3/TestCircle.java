package se.liu.ida.simja649.tddd78.lab3;

import java.util.ArrayList;

import static java.awt.Color.blue;

public class TestCircle

{
    public static void main(String[] args) {
	final ArrayList<Circle> circles = new ArrayList<>();
	Circle c1 = new Circle(1, 1, 1, blue);
	Circle c2 = new Circle(2, 10, 3, blue);
	Circle c3 = new Circle(6, 5, 4, blue);
	circles.add(c1);
	circles.add(c2);
	circles.add(c3);
	for (Circle circle : circles) {
	    int l = circle.getX();
	    int c = circle.getY();
	    System.out.println("x: " + l + " " + "y: " + c);

	}


    }
}
