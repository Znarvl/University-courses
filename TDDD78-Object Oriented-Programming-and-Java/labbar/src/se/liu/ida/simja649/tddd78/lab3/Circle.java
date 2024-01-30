package se.liu.ida.simja649.tddd78.lab3;

import java.awt.*;

public class Circle extends AbstractShape
{
    private int radius;


    public Circle(final int radius, final int x, final int y, final Color color) {
	super(x, y, color);
	if (radius < 0) {
	    throw new IllegalArgumentException("Negativ radie!");
	}
	this.radius = radius;

    }

    public int getRadius() {
	return radius;
    }

    @Override public String toString() {
	return "Circle{" + "radius=" + radius + ", x=" + getX() + ", y=" + getY() + ", color=" + getColor() + '}';
    }

    @Override public void draw(final Graphics g) {
	//System.out.println("Ritar: " + this);
	int diameter = 2 * radius;
	g.setColor(color);
	g.drawOval(x, y, diameter, diameter);

    }
}
