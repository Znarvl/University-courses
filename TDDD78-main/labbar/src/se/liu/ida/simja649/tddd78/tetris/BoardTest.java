package se.liu.ida.simja649.tddd78.tetris;

import javax.swing.*;
import java.awt.event.ActionEvent;

/**
 * Class where you connect all the classes to make a functioning game. You start the game here making the game move also with
 * tick
 */


public final class BoardTest
{

    private static final int BOARD_WIDTH = 10;
    private static final int BOARD_HEIGHT = 20;

    public static void main(String[] args) {

        Board board = new Board(BOARD_WIDTH, BOARD_HEIGHT);
        TetrisViewer t1 = new TetrisViewer(board);

        final Action update = new AbstractAction()
        {
            public void actionPerformed(ActionEvent e) {
                board.tick();
            }
        };

        final Timer clockTimer = new Timer(200, update);
        clockTimer.setCoalesce(true);
        clockTimer.start();

    }

}

