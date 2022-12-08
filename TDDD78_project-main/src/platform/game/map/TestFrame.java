package platform.game.map;

import platform.game.GameEngine;
import platform.game.objects.Player;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.nio.file.Watchable;

/**
 * test class to run the game. has the timer that updates the game.
 */

public class TestFrame
{
    private static Timer clockTimer;

    public static void main(String[] args) {
        Background background = new Background();
        Player player = new Player();

	GameEngine gameEngine = new GameEngine(player, background);
	WindowComponent windowComponent = new WindowComponent(gameEngine);
	new Viewer(windowComponent);



	final Action doOneStep = new AbstractAction() {

			public void actionPerformed(ActionEvent e) {

			    windowComponent.repaint();
			    gameEngine.gameTick(player);
			}
		    };

	clockTimer = new Timer(8, doOneStep);
	clockTimer.setCoalesce(true);
	clockTimer.start();
        }

}
