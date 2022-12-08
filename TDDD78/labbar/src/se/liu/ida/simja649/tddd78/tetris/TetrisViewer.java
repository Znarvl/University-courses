package se.liu.ida.simja649.tddd78.tetris;

import javax.swing.*;
import java.awt.*;

/**
 * Created a JFrame to tetris, which makes a window that shows up when you start the game
 */

public class TetrisViewer

{


    public TetrisViewer(Board gameBoard) {
	final JFrame frame = new JFrame("Tetris");
	frame.setLayout(new BorderLayout());
	final TetrisComponent comp = new TetrisComponent(gameBoard);
	frame.add(comp, BorderLayout.CENTER);
	frame.pack();
	frame.setSize(comp.getPreferredSize());
	frame.setVisible(true);
	gameBoard.addBoardListener(comp);


    }

}

