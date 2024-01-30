package platform.game.states;

import platform.game.map.WindowComponent;

import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

/**
 * Class used to make the click function in menu work
 */

public class MouseInput extends MouseAdapter

{

    @Override public void mousePressed(final MouseEvent e) {
        int clickX = e.getX();
        int clickY = e.getY();


	//PLAY
	if (WindowComponent.getState() == State.MENU) {
	    if (clickX >= 375 && clickX <= 575) {
		if (clickY >= 230 && clickY <= 290) {
		    WindowComponent.setState(State.GAME);
		}
	    }
	    //Instructions
	    if (clickX >= 375 && clickX <= 575) {
		if (clickY >= 300 && clickY <= 360) {
		    WindowComponent.setState(State.INSTRUCTIONS);
		}
	    }
	}

	//if in instuctions, go back to menu
	if (WindowComponent.getState() == State.INSTRUCTIONS) {
	    if (clickX >= 375 && clickX <= 575) {
		if (clickY >= 450 && clickY <= 510) {
		    WindowComponent.setState(State.MENU);
		}
	    }
	}

    }

}
