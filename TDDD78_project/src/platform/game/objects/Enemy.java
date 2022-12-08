package platform.game.objects;

import platform.game.map.Background;
import javax.swing.*;
import java.awt.*;

/**
 * Keeps track of the enemys' possition, dimensions and the spawnings of them.
 */

public class Enemy
{
    private int x;
    private int y;
    public Image img;
    public static final int ENEMYHEIGHT = 64;
    public static final int ENEMYWIDTH = 64;


    public Enemy(final int y) {
	ImageIcon i =  new ImageIcon(this.getClass().getResource("/enemy.png"));
	this.x = Background.IMAGE_WIDTH;
	this.y = y;
	this.img = i.getImage();

    }

    public int getX () {
	return x;
    }

    public int getY () {
	return y;
    }

    // We have Top because makes the collisionhandler easier to understand (in player)
    public int getTop() {
	return y;
    }

    public int getBottom() {
	return y + ENEMYHEIGHT;
    }

    // We have Left because makes the collisionhandler easier to understand (in player)
    public int getLeft() {
	return x;
    }

    public int getRight() {
	return x + ENEMYWIDTH;
    }

    public void enemyTick() {
	    this.x -= 1;
	}
}

