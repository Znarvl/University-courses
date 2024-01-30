package se.liu.ida.simja649.tddd78.tetris;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.EnumMap;

/**
 * This class renders(paints) the board and all the Tetrominos also is used to give input to the arrow keys to move tetros
 */


public class TetrisComponent extends JComponent implements BoardListener
{
    private Board gameBoard;
    private final static int RECT_SIDE_LENGTH = 30;
    private EnumMap<SquareType, Color> colorEnumMap;


    public TetrisComponent(Board gameBoard) {

	gameBoard.addBoardListener(this);

	this.gameBoard = gameBoard;

	this.colorEnumMap = new EnumMap<>(SquareType.class);
	colorEnumMap.put(SquareType.EMPTY, Color.LIGHT_GRAY);
	colorEnumMap.put(SquareType.I, Color.RED);
	colorEnumMap.put(SquareType.J, Color.YELLOW);
	colorEnumMap.put(SquareType.L, Color.MAGENTA);
	colorEnumMap.put(SquareType.O, Color.ORANGE);
	colorEnumMap.put(SquareType.S, Color.GREEN);
	colorEnumMap.put(SquareType.T, Color.BLUE);
	colorEnumMap.put(SquareType.Z, Color.CYAN);
	colorEnumMap.put(SquareType.OUTSIDE, Color.BLACK);
	final InputMap in = this.getInputMap(JComponent.WHEN_IN_FOCUSED_WINDOW);
	in.put(KeyStroke.getKeyStroke("LEFT"), "left");
	in.put(KeyStroke.getKeyStroke("RIGHT"), "right");
	in.put(KeyStroke.getKeyStroke("UP"), "up");

	final ActionMap act = this.getActionMap();
	act.put("left", new newMoveLeft());
	act.put("right", new newMoveRight());
	act.put("up", new newRotate());


    }

    private class newMoveLeft extends AbstractAction
    {
	@Override public void actionPerformed(final ActionEvent e) {
	    gameBoard.moveLeft();
	}
    }

    private class newRotate extends AbstractAction
    {
	@Override public void actionPerformed(final ActionEvent e) {
	    gameBoard.rotate();
	}

    }

    private class newMoveRight extends AbstractAction
    {
	@Override public void actionPerformed(final ActionEvent e) {
	    gameBoard.moveRight();

	}
    }

    public Dimension getPreferredSize() {
	return new Dimension(gameBoard.getWidth() * RECT_SIDE_LENGTH, gameBoard.getHeight() * RECT_SIDE_LENGTH);
    }


    @Override protected void paintComponent(Graphics g) {
	super.paintComponent(g);
	final Graphics2D g2d = (Graphics2D) g;

	for (int i = 0; i < gameBoard.getHeight(); i++) {
	    for (int j = 0; j < gameBoard.getWidth(); j++) {
		SquareType square = gameBoard.getSquareTypeAt(j, i);
		g2d.setColor(colorEnumMap.get(square));
		g2d.fillRect(j * RECT_SIDE_LENGTH, i * RECT_SIDE_LENGTH, RECT_SIDE_LENGTH, RECT_SIDE_LENGTH);

	    }

	}

    }


    @Override public void boardChanged() {
	this.repaint();
    }
}
