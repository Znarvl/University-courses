package platform.game.map;

import javax.swing.*;
import java.awt.*;

/**
 * Keeps track of the background and dimensions of it
 */

public class Background extends JPanel
{
    private static final int BOTTOM = 532;
    public Image img;
    private int x;
    public static final int IMAGE_WIDTH = 1000;
    private static final int TOP = 0;


    public Background(){
        this.x = 0;
        ImageIcon i = new ImageIcon(this.getClass().getResource("/background.jpg"));

        setFocusable(true);
        this.img = i.getImage();
    }

    public void setX(final int x) {
        this.x = x;
    }

    public int getX() {
        return x;
    }

    public static int getBottom() {
        return BOTTOM;
    }

    public static int getTop() {
        return TOP;
    }
}
