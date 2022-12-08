package se.liu.ida.simja649.tddd78.tetris;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


/**
 * Class creates a board, it checks collisions of the poly and remove rows
 */

class Board
{
    private final SquareType[][] squares;
    private final int width;
    private final int height;
    private int fallingY;
    private int fallingX;
    private Poly falling = null;
    private final static int BOARD_OFFSET = 2;
    private List<BoardListener> listners;


    Board(final int width, final int height) {
        listners = new ArrayList<>();
        this.width = width;
        this.height = height;
        this.fallingY = 0;
        this.fallingX = 0;
        this.squares = new SquareType[height + 4][width + 4];

        //make sure there are 2 outside "blocks", if not, it is empty
        for (int i = 0; i < height + 4; i++) {
            for (int j = 0; j < width + 4; j++) {
                if (j < BOARD_OFFSET || j >= width + BOARD_OFFSET || i < BOARD_OFFSET || i >= height + BOARD_OFFSET) {
                    squares[i][j] = SquareType.OUTSIDE;

                } else {
                    squares[i][j] = SquareType.EMPTY;
                }

            }
        }
        this.notifyListeners();
    }

    // tittar board och fallande obj
    public SquareType getSquareTypeAt(int x, int y) {

        if (falling != null) {

            int x1 = fallingX;
            int x2 = x1 + falling.getWidth() - 1;
            int y1 = fallingY;
            int y2 = y1 + falling.getHeight() - 1;

            // if not between, can't be a falling poly
            if (x < x1 || x > x2 || y < y1 || y > y2) {
                return squares[y + BOARD_OFFSET][x + BOARD_OFFSET];
                // Watch scope of poly, if empty, return board squaretype
            } else if (falling.getSquareType(x - x1, y - y1) == SquareType.EMPTY) {
                return squares[y + BOARD_OFFSET][x + BOARD_OFFSET];
            } else {
                //when having no EMPTY space
                return falling.getSquareType(x - x1, y - y1);

            }
        }
        return squares[y + BOARD_OFFSET][x + BOARD_OFFSET];
    }


    private boolean hasCollision() {
        for (int i = 0; i < falling.getHeight(); i++) {
            for (int j = 0; j < falling.getWidth(); j++) {
                if (falling.getSquare(j, i) != SquareType.EMPTY && getBoardSquare(j + fallingX, i + fallingY) != SquareType.EMPTY) {
                    return true;
                }
            }
        }
        return false;

    }


    private void landed() {
        for (int n = 0; n < falling.getHeight(); n++) {
            for (int j = 0; j < falling.getWidth(); j++) {
                if (falling.getSquare(j, n) != SquareType.EMPTY) {
                    squares[fallingY + n + BOARD_OFFSET][fallingX + j + BOARD_OFFSET] = falling.getSquare(j, n);
                }
            }
        }
    }

    public SquareType getBoardSquare(int x, int y) {
        return squares[y + 2][x + 2];
    }

    public void rotate() {
        if (falling != null) {
            Poly lastState = falling;
            falling = falling.rotateRight();
            if (hasCollision()) {
                falling = lastState;
            }
        }
        notifyListeners();
    }

    public void moveRight() {
        if (falling != null) {
            fallingX += 1;

            if (hasCollision()) {
                fallingX -= 1;
            }
        }
        notifyListeners();
    }

    public void moveLeft() {
        if (falling != null) {
            fallingX -= 1;
            if (hasCollision()) {
                fallingX += 1;
            }
        }
        notifyListeners();
    }

    private void removeRow() {
        for (int i = 0; i < height; i++) {
            // if full row = true
            boolean full = true;
            for (int j = 0; j < width; j++) {
                if (getBoardSquare(j, i) == SquareType.EMPTY) {
                    full = false;

                }
            }
            // if boolean full is true, enter if statement
            if (full) {
                for (int b = 0; b < width; b++) {
                    squares[i + BOARD_OFFSET][b + BOARD_OFFSET] = SquareType.EMPTY;
                }
                //places row above one step down
                for (int j = i; j > 0; j--) {
                    for (int t = 0; t < width; t++) {
                        //places already static squares
                        squares[j + 2][t + 2] = squares[j + 1][t + 2];

                    }

                }
            }
        }
    }

    public void tick() {
        if (falling == null) {
            spawnPoly();
        }
        fallingY++;
        if (hasCollision()) {
            fallingY--;
            landed();
            removeRow();
            spawnPoly();
        }

        notifyListeners();
    }

    private void spawnPoly() {
        Random rand = new Random();
        this.falling = TetrominoMaker.getPoly(rand.nextInt(TetrominoMaker.getNumberOfTypes()));
        this.fallingX = (width / 2) - 1;
        this.fallingY = 1;
        if (hasCollision()) {
            System.exit(0);
        }


    }

    public void addBoardListener(BoardListener bl) {
        listners.add(bl);
    }

    private void notifyListeners() {
        for (BoardListener listener : listners) {
            listener.boardChanged();
        }
    }


    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

}

