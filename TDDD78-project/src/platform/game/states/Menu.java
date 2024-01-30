package platform.game.states;

import platform.game.map.Viewer;

import java.awt.*;

/**
 * Used to render the meny of game, shows text and other significant information to player. Rectangles used
 * to click in
 */

public class Menu

{
    private final static int BOX_WIDTH = 200;
    private final static int BOX_HEIGHT =  60;
    private Rectangle play 	 =  new Rectangle((int)Viewer.WIDTH / 2 - BOX_WIDTH / 2, 230, BOX_WIDTH, BOX_HEIGHT);
    private Rectangle instruction =  new Rectangle((int)Viewer.WIDTH / 2 - BOX_WIDTH / 2, 300, BOX_WIDTH, BOX_HEIGHT);

    public void render(Graphics g){
        Graphics2D g2d = (Graphics2D) g;
	Font fnt = new Font("arial", Font.BOLD, 50);
   	g.setFont(fnt);
   	g.setColor(Color.white);
   	g.drawString("EPIC REEEE", Viewer.WIDTH /2 - 150, 200 );
	Font fnt1 = new Font("times", Font.BOLD, 40);
	g.setFont(fnt1);
	g.drawString("Play", Viewer.WIDTH /2 - 40,275);
	Font fnt2 = new Font("times", Font.BOLD, 35);
	g.setFont(fnt2);
	g.drawString("Instructions", Viewer.WIDTH /2 - 90,345);
   	g2d.draw(play);
   	g2d.draw(instruction);

    }
}
