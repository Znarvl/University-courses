package platform.game.objects;

import platform.game.map.Background;
import platform.game.map.Viewer;

/**
 * Keeps track of the possition of the bullets the player shoots. Aswell as how it should move.
 */

public class Bullet
{
    private int vertVelocity;
    private int horiVelocity;
    private int x;
    private int y;
    private final int GUNALIGNERY = 20;
    private final int GUNALIGNERX = 48;

    public Bullet(Player shooter) {

	final int VELOCITY = 10;
	if (shooter.isDucking()){
            this.vertVelocity = -1 * VELOCITY;
            this.horiVelocity = 0;
            this.x = shooter.getX() - GUNALIGNERX;
            this.y = shooter.getY() + GUNALIGNERY;
	}

        else {
            this.horiVelocity = VELOCITY;
            this.vertVelocity = 0;
	    this.x = shooter.getX() + GUNALIGNERX;
	    this.y = shooter.getY() + GUNALIGNERY;
	}
    }


    public int getX() {
	return x;
    }

    public int getY() {
	return y;
    }



    public void bulletTick(){
	this.x += this.horiVelocity;
	this.y += this.vertVelocity;
    }

    public boolean hitEnemy(Enemy enemy) {
	return (this.y >= enemy.getTop() && this.y <= enemy.getBottom() &&
		this.x >= enemy.getLeft() && this.x <= enemy.getRight());
    }


    public boolean outOfView() {
	return (x >= Viewer.getWIDTH() || y <= Background.getTop());
    }


}
