package se.liu.ida.simja649.tddd78.lab3;

import java.awt.*;
import java.util.ArrayList;


public class TestShapes

{
    public static void main(String[] args) {
	final ArrayList<Shape> shapes = new ArrayList<>();
	shapes.add(new Circle(50, 50, 50, Color.MAGENTA));
	shapes.add(new Circle(50, 50, 30, Color.RED));
	shapes.add(new Circle(50, 50, 10, Color.BLUE));

	shapes.add(new Rectangle(30, 40, 40, 50, Color.BLUE));

	shapes.add(new Text(10, 20, Color.RED, "Fiskmås"));

	for (Shape shape : shapes) {
	    // shape.draw();
	}


    }
}
