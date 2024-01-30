package interpreter.lisp;


public class Eq extends BinaryExpression<Expr> {

	@Override
	Expr evalBinaryExpression(Expr value1, Expr value2) {
		return value1.equals(value2) ? Constants.TRUE : Constants.FALSE;
	}
	
}
