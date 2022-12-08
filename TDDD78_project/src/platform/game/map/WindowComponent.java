package platform.game.map;

import platform.game.GameEngine;
import platform.game.objects.Bullet;

import platform.game.objects.Enemy;
import platform.game.objects.Player;
import platform.game.objects.PowerUp;
import platform.game.states.Instructions;
import platform.game.states.MouseInput;
import platform.game.states.State;
import platform.game.states.Menu;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.geom.AffineTransform;

/**
 * Paints everything looks for key presses
 */

public class WindowComponent extends JComponent
{
    private Player player;
    private Background board;
    private static State state = State.MENU;
    private final static int PADDING = 20;

    private GameEngine gameEngine;


    public WindowComponent(GameEngine engine) {
	this.gameEngine = engine;
	this.player = gameEngine.getPlayer();
	this.board = gameEngine.getBackground();

	this.addMouseListener(new MouseInput());

	final InputMap in = this.getInputMap(JComponent.WHEN_IN_FOCUSED_WINDOW);
		in.put(KeyStroke.getKeyStroke("LEFT"), "left");
		in.put(KeyStroke.getKeyStroke("RIGHT"), "right");
		in.put(KeyStroke.getKeyStroke("UP"), "up");
		in.put(KeyStroke.getKeyStroke("DOWN"), "down");
		in.put(KeyStroke.getKeyStroke("SPACE"), "space");

		final ActionMap act = this.getActionMap();
		act.put("left", new MoveLeft());
		act.put("right", new MoveRight());
		act.put("up", new Jump());
		act.put("down", new Duck());
		act.put("space", new Shoot());
    }


    private class MoveLeft extends AbstractAction {
	@Override public void actionPerformed(final ActionEvent e) {
	    if (state == State.GAME) {
		player.moveLeft();
	    }
	}
    }

    private class MoveRight extends AbstractAction {
        @Override public void actionPerformed(final ActionEvent e) {
	    if (state == State.GAME) {
		player.moveRight();

	    }
	}
    }

    private class Jump extends AbstractAction {
        @Override public void actionPerformed(final ActionEvent e) {
	    if (state == State.GAME) {
		player.jump();
	    }
	}
    }

    private class Duck extends AbstractAction {
        @Override public void actionPerformed(final ActionEvent e) {
	    if (state == State.GAME) {
		player.duck();
	    }
	}
    }

    private class Shoot extends AbstractAction {
        @Override public void actionPerformed(final ActionEvent e) {
	    if (state == State.GAME) {
		gameEngine.shoot();
	    }
	}
    }



    @Override protected void paintComponent(Graphics g){
        super.paintComponent(g);
	Menu menu = new Menu();

	Instructions instruction = new Instructions();
	Graphics2D g2d =  (Graphics2D) g;

	if (player.moveBoard()){
	    board.setX(board.getX() - (int)player.getHorizontalVelocity());
	    for (PowerUp powerUp : gameEngine.getPowerUpList()){
	        powerUp.setX(powerUp.getX() - (int) player.getHorizontalVelocity());
	    }
	}
	
	int image1Pos = board.getX();
	int image2Pos = board.getX() + board.IMAGE_WIDTH;


	if (image1Pos <= -board.IMAGE_WIDTH){
	    board.setX(0);
	}

	g2d.drawImage(board.img, image1Pos,0, null);
	g2d.drawImage(board.img, image2Pos, 0, null);




	if (state == State.MENU){

	    menu.render(g);
	}

	if (state == State.INSTRUCTIONS){
	    instruction.render(g);
	}



	if (state == State.GAME) {
	    AffineTransform backup = g2d.getTransform();
	    AffineTransform a = AffineTransform.getRotateInstance(4.71, player.getX(), player.getY() + Player.getPLAYERHEIGHT());


	    for (Bullet bullet : gameEngine.getBulletList()) {
		g2d.fillRect(bullet.getX(), bullet.getY(), 5, 5);
	    }

	   for (Enemy enemy : gameEngine.getStillLivingEnemies()) {
	       g2d.drawImage(enemy.img, enemy.getX(), enemy.getY(), null);
	   }

	   for (PowerUp powerUp : gameEngine.getPowerUpList()) {
	       g2d.setColor(Color.ORANGE);
	       g2d.fillRect(powerUp.getX(), powerUp.getY(), powerUp.WIDTH, powerUp.HEIGHT);
	   }


	    g2d.setColor(Color.GREEN);
	    g2d.fillRect(PADDING, PADDING, player.getHealth()*20, 30);

	    g2d.setColor(Color.RED);
	    g2d.fillRect(PADDING + player.getHealth()*20, PADDING, (player.getmaxHealth() - player.getHealth()) * 20, 30);

	    if (player.isDucking()) {
		g2d.setTransform(a);
	    } else {
		g2d.setTransform(backup);
	    }

	    if (player.isPoweredUp()) {
		g2d.drawImage(player.opImg, player.getX(), player.getY(), null);
	    }
	    else{
		g2d.drawImage(player.img, player.getX(), player.getY(), null);
	    }


	}

    }

    public static State getState() {
	return state;
    }

    public static void setState(final State state) {
	WindowComponent.state = state;
    }

}



