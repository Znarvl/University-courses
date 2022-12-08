package platform.game.objects;

import platform.game.map.Background;
import platform.game.map.Viewer;

import javax.swing.*;
import java.awt.*;


/**
 * Central class that represent the player. Handles movement and collisions between all objects
 */

public class Player
{
    public Image img;
    public Image opImg;
    protected int height;
    protected int width;
    private static final int PLAYERHEIGHT = 72;
    private static final int PLAYERWIDTH = 48;
    private int x, y, health;
    private final static int MAX_HEALTH = 10;
    private boolean ducking;
    private int top;
    private int bottom;
    private int left;
    private int right;

    private double verticalVelocity;
    private double horizontalVelocity;
    private final static double VERTICAL_ACCELERATION = 0.005;
    private final static double HORIZONTAL_ACCELERATION = 0.05;
    private int fallingTime;
    private boolean falling;

    private int shootDelay;
    private int shootTimer;
    private final static int POWERUP_TIME = 1000 / 8 * 5;
    private boolean poweredUp;
    private int beenPowerdUp;

    private final static int DEFAULTSHOOTDELAY = 60;
    private int rapidShooting;



    public Player() {

        //apperence
        ImageIcon i  = new ImageIcon(this.getClass().getResource("/dude.png"));
        ImageIcon i2 = new ImageIcon(this.getClass().getResource("/RAPIDFIREdude.png"));
        this.img     = i.getImage();
        this.opImg   = i2.getImage();
        this.ducking = false;
	this.x 	     = 30;
	this.y 	     = Background.getBottom() - PLAYERHEIGHT;
	this.health  = MAX_HEALTH;
	this.height  = PLAYERHEIGHT;
	this.width   = PLAYERWIDTH;


	//physics
	this.horizontalVelocity = 0;
	this.verticalVelocity 	= 0;
	this.fallingTime 	= 0;
	this.falling 		= true;

	//shooting, removal of objects and powerUp
	this.shootDelay    = DEFAULTSHOOTDELAY;
	this.shootTimer    = shootDelay;
	this.rapidShooting = DEFAULTSHOOTDELAY /3;
	this.beenPowerdUp  = 0;
	this.poweredUp	   = false;




    }

    // Getters


    public static int getPLAYERHEIGHT() {
	return PLAYERHEIGHT;
    }

    public int getX() {
	return x;
    }

    public int getY() {
	return y;
    }

    public int getHealth() {
	return health;
    }

    public int getmaxHealth() {
	return MAX_HEALTH;
    }

    public boolean isDucking() {
	return ducking;
    }

    public boolean isPoweredUp() {
	return poweredUp;
    }

    public int getShootDelay() {
	return shootDelay;
    }

    public int getShootTimer() {
	return shootTimer;
    }

    public double getHorizontalVelocity() {
	return horizontalVelocity;
    }

    public int getBottom() {
	return bottom;
    }

    public int getLeft() {
	return left;
    }

    public int getRight() {
	return right;
    }

    //setter
    public void setPos(){
   	this.top     = y;
     	this.bottom  = y + height;
     	this.left    = x;
     	this.right   = x + width;
    }

    public void setHealth(final int health) {
	this.health = health;
    }

    public void setPoweredUp(final boolean poweredUp) {
	this.poweredUp = poweredUp;
    }

    public void setBeenPowerdUp(final int beenPowerdUp) {
	this.beenPowerdUp = beenPowerdUp;
    }

    public void setShootTimer(final int shootTimer) {
	this.shootTimer = shootTimer;
    }

    // Movement
    public void jump() {
	verticalVelocity = -10;
	falling = true;
	stopDucking();
    }

    public void duck() {
        startDucking();
    }

    public void moveRight() {
        horizontalVelocity = 6;
        stopDucking();
    }

    public void moveLeft() {
	horizontalVelocity = -6;
	stopDucking();
    }

    @SuppressWarnings("SuspiciousNameCombination") public void startDucking(){
	if (!ducking){
	    x += height;
	}
	ducking = true;
    }

    @SuppressWarnings("SuspiciousNameCombination") public void stopDucking(){
	if(ducking){
	    x -= height;
	}
	ducking = false;
    }

    public boolean moveBoard() {
	return (x >= Viewer.WIDTH / 2 - PLAYERWIDTH / 2);
    }


    public void playerTick(){
	setPos();


	//Shoot and enemy things
	shootTimer += 1;
	if (shootTimer > shootDelay) {
	    shootTimer = shootDelay;
	}



	// Handle powerup

	if (poweredUp) {
	   	        shootDelay = rapidShooting;
	   	        beenPowerdUp += 1;
	   	        if (beenPowerdUp >= POWERUP_TIME){
	   	            poweredUp = false;
	   	            beenPowerdUp = 0;
	   	            shootDelay = DEFAULTSHOOTDELAY;
	   		}
	}

	// Movement things

	if (ducking) {
	    height = PLAYERWIDTH;
	    width = PLAYERHEIGHT;
	} else {
	    height = PLAYERHEIGHT;
	    width = PLAYERWIDTH;
	}


	if (falling) {
	    fallingTime += 1;
	} else {
	    fallingTime = 0;
	}


	if (verticalVelocity < 10) {
	    verticalVelocity += VERTICAL_ACCELERATION * fallingTime;
	} else {
	    verticalVelocity = 10;
	}


	y += (int) verticalVelocity;


	if (y > Background.getBottom() - PLAYERHEIGHT) {
	    y = Background.getBottom() - PLAYERHEIGHT;

	    if (horizontalVelocity < 0) {
		horizontalVelocity += HORIZONTAL_ACCELERATION * 2;
		if (horizontalVelocity > 0) {
		    horizontalVelocity = 0;
		}
	    }

	    if (horizontalVelocity > 0) {
		horizontalVelocity -= HORIZONTAL_ACCELERATION * 2;
		if (horizontalVelocity < 0) {
		    horizontalVelocity = 0;
		}
	    }

	    falling = false;
	}

	if (!moveBoard() || horizontalVelocity < 0) {
	    x += (int) horizontalVelocity;
	    if (x < 0) {
		x = 0;
		horizontalVelocity = 0;
	    }
	}


	if (x > Background.IMAGE_WIDTH / 2 - width / 2) {
	    x = Background.IMAGE_WIDTH / 2 - width / 2;
	}

	if (y < Background.getTop()) {
	    y = Background.getTop();
	}

    }

    public boolean hasCollision(final Enemy enemy) {
	return ((left >= enemy.getLeft() && left <= enemy.getRight() &&
		top >= enemy.getTop() && top <= enemy.getBottom()) ||
		(right >= enemy.getLeft() && right <=enemy.getRight() &&
		bottom >= enemy.getTop() && bottom <= enemy.getBottom()));

    }




}
