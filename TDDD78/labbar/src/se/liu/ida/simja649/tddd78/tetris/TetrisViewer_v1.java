package se.liu.ida.simja649.tddd78.tetris;

import javax.swing.*;
import java.awt.*;

/**
 * Not used anymore, was used before to test JFrame
 */

public class TetrisViewer_v1

{
    private Board gameboard;


    public TetrisViewer_v1(Board gameBoard) {
	final JFrame frame = new JFrame("Tetris");
	this.gameboard = gameboard;

	frame.setLayout(new BorderLayout());
	JTextArea textarea = new JTextArea(gameBoard.getWidth(), gameBoard.getHeight());
	frame.add(textarea, BorderLayout.CENTER);
	textarea.setText(BoardToTextConverter.convertToText(gameBoard));
	textarea.setFont(new Font("Monospaced", Font.PLAIN, 20));
	frame.pack();
	frame.setVisible(true);


    }


}

