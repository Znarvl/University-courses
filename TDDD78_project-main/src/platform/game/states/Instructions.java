package platform.game.states;

import platform.game.map.Viewer;

import java.awt.*;

/**
 * Rendering class with the function to show player how the game works
 * rectangle works as a notifyer where to click
 */

public class Instructions
{
    private Rectangle back =  new Rectangle(Viewer.WIDTH / 2 - 100, 450, 200, 60);

    public void render(Graphics g) {
	Graphics2D g2d = (Graphics2D) g;
	Font fnt = new Font("arial", Font.BOLD, 50);
	g.setFont(fnt);
	g.setColor(Color.white);
	g.drawString("Instructions", 325, 200);
	Font fnt1 = new Font("times", Font.BOLD, 40);
	g.setFont(fnt1);
	g.drawString("Move", 300, 275);
	g.drawString("Arrows", 300, 345);
	g.drawString("Shoot", 500, 275);
	g.drawString("Space", 500, 345);

	g.drawString("Back", Viewer.WIDTH / 2 - 45, 495);



	g2d.draw(back);



    }
}
