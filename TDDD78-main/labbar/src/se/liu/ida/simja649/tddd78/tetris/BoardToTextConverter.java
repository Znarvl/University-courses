package se.liu.ida.simja649.tddd78.tetris;


/**
 * Class not used anymore, used before to test when it was text based
 */


public final class BoardToTextConverter
{

    public static String convertToText(Board board) {
        StringBuilder builder = new StringBuilder();
        for (int col = 0; col < board.getHeight(); col++) {
            for (int row = 0; row < board.getWidth(); row++) {

		SquareType square = board.getSquareTypeAt(col, row);

                switch (square) {
                    case EMPTY:
                        builder.append("-");
			break;
		    case OUTSIDE:
			builder.append("#");
                        break;
                    case I:
                        builder.append("#");
                        break;
                    case O:
                        builder.append("&");
                        break;
                    case T:
                        builder.append("%");
                        break;
                    case S:
                        builder.append("=");
                        break;
                    case Z:
                        builder.append("+");
                        break;
                    case J:
                        builder.append("@");
                        break;
                    case L:
                        builder.append("$");
                        break;

                }
            }
            builder.append("\n");

        }
        return builder.toString();
    }
}
