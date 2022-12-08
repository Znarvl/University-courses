package platform.game.objects;

@SuppressWarnings("SuspiciousGetterSetter")
/**
 * Keeps track of the possiotion and dimensions of the powerup
 */

public class PowerUp
{
    private int x;
    private int y;
    public final static int HEIGHT = 40;
    public final static int WIDTH = 40;

    public PowerUp(final int x, final int y) {
	this.x = x;
	this.y = y;
    }

    public int getX() {
	return x;
    }

    public int getY() {
	return y;
    }

    public int getTop() {
	return y;
    }

    public int getLeft() {
	return x;
    }

    public int getRight() {
	return x + WIDTH;
    }

    public void setX(final int x) {
	this.x = x;
    }
}
