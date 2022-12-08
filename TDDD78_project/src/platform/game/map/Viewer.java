package platform.game.map;

import platform.game.GameEngine;
import platform.game.objects.Player;

import javax.swing.*;

/**
 * creasts a window and sets it's dimensions and add all the things to the window.
 */

public class Viewer
{
    public final static int WIDTH = 900;
    public final static int HEIGHT = 600;


    public Viewer(WindowComponent windowComponent){


	JFrame frame = new JFrame();
	frame.add(windowComponent);
	frame.setTitle("Scroller REEE");
	frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
	frame.setSize(WIDTH, HEIGHT);
	frame.setVisible(true);
	frame.setResizable(false);
	frame.setLocationRelativeTo(null);
    }


    public static int getWIDTH() {
	return WIDTH;
    }

}
