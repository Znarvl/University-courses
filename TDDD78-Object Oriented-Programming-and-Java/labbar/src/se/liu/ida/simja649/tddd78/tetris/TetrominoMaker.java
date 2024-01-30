package se.liu.ida.simja649.tddd78.tetris;

/**
 * Class creates the tetrominos and their shapes
 */


public final class TetrominoMaker
{

    public static int getNumberOfTypes() {
	return SquareType.values().length - 2;
    }

    public static Poly getPoly(int n) {
	switch (n) {
	    case 0: {
		Poly poly = new Poly(4, 4);
		fillEmpty(poly);
		createPolyI(poly);
		return poly;
	    }
	    case 1: {
		Poly poly = new Poly(2, 2);
		fillEmpty(poly);
		createPolyO(poly);
		return poly;
	    }
	    case 2: {
		Poly poly = new Poly(3, 3);
		fillEmpty(poly);
		createPolyZ(poly);
		return poly;
	    }
	    case 3: {
		Poly poly = new Poly(3, 3);
		fillEmpty(poly);
		createPolyT(poly);
		return poly;
	    }
	    case 4: {
		Poly poly = new Poly(3, 3);
		fillEmpty(poly);
		createPolyL(poly);
		return poly;
	    }
	    case 5: {
		Poly poly = new Poly(3, 3);
		fillEmpty(poly);
		createPolyJ(poly);
		return poly;
	    }
	    case 6:
		Poly poly = new Poly(3, 3);
		fillEmpty(poly);
		createPolyS(poly);
		return poly;
	}
	throw new IllegalArgumentException("invalid index" + n);
    }

    private static void fillEmpty(Poly block) {
	for (int width = 0; width < block.getWidth(); width++) {
	    for (int height = 0; height < block.getHeight(); height++) {
		block.setShape(width, height, SquareType.EMPTY);
	    }
	}
    }

    private static void createPolyI(Poly shape) {
	shape.setShape(0, 1, SquareType.I);
	shape.setShape(1, 1, SquareType.I);
	shape.setShape(2, 1, SquareType.I);
	shape.setShape(3, 1, SquareType.I);
    }

    private static void createPolyJ(Poly shape) {
	shape.setShape(0, 0, SquareType.J);
	shape.setShape(0, 1, SquareType.J);
	shape.setShape(1, 1, SquareType.J);
	shape.setShape(2, 1, SquareType.J);
    }

    private static void createPolyL(Poly shape) {
	shape.setShape(2, 0, SquareType.L);
	shape.setShape(0, 1, SquareType.L);
	shape.setShape(1, 1, SquareType.L);
	shape.setShape(2, 1, SquareType.L);
    }

    private static void createPolyO(Poly shape) {
	shape.setShape(0, 0, SquareType.O);
	shape.setShape(0, 1, SquareType.O);
	shape.setShape(1, 0, SquareType.O);
	shape.setShape(1, 1, SquareType.O);
    }

    private static void createPolyS(Poly shape) {
	shape.setShape(1, 0, SquareType.S);
	shape.setShape(2, 0, SquareType.S);
	shape.setShape(0, 1, SquareType.S);
	shape.setShape(1, 1, SquareType.S);
    }

    private static void createPolyT(Poly shape) {
	shape.setShape(1, 0, SquareType.T);
	shape.setShape(0, 1, SquareType.T);
	shape.setShape(1, 1, SquareType.T);
	shape.setShape(2, 1, SquareType.T);
    }

    private static void createPolyZ(Poly block) {
	block.setShape(0, 0, SquareType.Z);
	block.setShape(1, 0, SquareType.Z);
	block.setShape(1, 1, SquareType.Z);
	block.setShape(2, 1, SquareType.Z);
    }
}
