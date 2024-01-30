package se.liu.ida.simja649.tddd78.tetris;

/**
 * Creates a poly of spec width and height that we can see in board also rotates poly
 */

public class Poly {
    private SquareType[][] shape;
    private int height;
    private int width;


    public Poly(final int width, final int height) {
        this.height = height;
        this.width = width;
        this.shape = new SquareType[height][width];


    }

    public SquareType getSquare(int x, int y) {
        if (shape[y][x] != null) {
            return shape[y][x];
        } else {
            return SquareType.EMPTY;
        }
    }


    public int getHeight() {
        return height;
    }

    public int getWidth() {
        return width;
    }


    public SquareType getSquareType(int width, int height) {
        return shape[height][width];
    }

    public void setShape(int width, int height, SquareType block) {

        this.shape[height][width] = block;
    }


    // changed the size to height and width
    public Poly rotateRight() {
        Poly newPoly = new Poly(height, width);
        for (int r = 0; r < height; r++) {
            for (int c = 0; c < width; c++) {
                newPoly.shape[c][height - 1 - r] = this.shape[r][c];
            }
        }

        return newPoly;
    }


}
