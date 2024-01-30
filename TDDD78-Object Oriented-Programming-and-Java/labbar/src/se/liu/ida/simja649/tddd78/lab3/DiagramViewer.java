package se.liu.ida.simja649.tddd78.lab3;

import javax.swing.*;
import java.awt.*;
import java.util.List;
import java.util.Random;

public class DiagramViewer
{
    private final static List<Color> COLORS =
	    List.of(Color.BLACK, Color.RED, Color.GREEN, Color.BLUE, Color.CYAN, Color.YELLOW, Color.MAGENTA);

    // Set a fixed seed 0 so you always get the same
    // shapes (for debugging)
    public static Random rnd = new Random(2);

    private static Color getRandomColor() {
	return COLORS.get(rnd.nextInt(COLORS.size()));
    }

    private static Circle getRandomCircle() {
	return new Circle(rnd.nextInt(400), rnd.nextInt(400), rnd.nextInt(200), getRandomColor());
    }

    private static Rectangle getRandomRectangle() {
	return new Rectangle(rnd.nextInt(400), rnd.nextInt(400), rnd.nextInt(200), rnd.nextInt(200), getRandomColor());
    }

    private static Text getRandomText() {
	return new Text(rnd.nextInt(400), rnd.nextInt(400), getRandomColor(), "Hello");
    }

    public static void main(String[] args) {

	DiagramComponent comp = new DiagramComponent();

	Random rnd = new Random(0);

	for (int i = 0; i < 10; i++) {
	    switch (rnd.nextInt(3)) {
		case 0:
		    comp.addShape(getRandomCircle());
		    break;
		case 1:
		    comp.addShape(getRandomRectangle());
		    break;
		case 2:
		    comp.addShape(getRandomText());
		    break;
	    }

	}

	JFrame frame = new JFrame("Mitt fönster");
	frame.setLayout(new BorderLayout());
	frame.add(comp, BorderLayout.CENTER);
	frame.setSize(800, 600);
	frame.setVisible(true);
    }
}

