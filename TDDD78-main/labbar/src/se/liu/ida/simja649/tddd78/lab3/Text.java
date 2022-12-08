package se.liu.ida.simja649.tddd78.lab3;

import java.awt.*;

public class Text extends AbstractShape
{

    private int size;
    private String text;

    public Text(final int x, final int y, final Color color, final String text) {
	super(x, y, color);
	this.size = x * y;
	this.text = text;
    }


    public int getSize() {
	return size;
    }


    public String getText() {
	return text;
    }

    @Override public String toString() {
	return "Text{" + "x=" + x + ", y=" + y + ", size=" + size + ", color=" + color + ", text='" + text + '\'' + '}';
    }

    @Override public void draw(final Graphics g) {
	g.setColor(color);
	g.setFont(new Font("serif", Font.PLAIN, 20));
	g.drawString(text, x, y);

    }
}
