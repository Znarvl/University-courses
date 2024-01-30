package interpreter.lisp;

public class Sub extends BinaryExpression<Num> {

	/**
	 * 
	 * We assume that the operands have been evaluated to Num objects
	 * 
	 * @see interpreter.lisp.BinaryExpression#evalBinaryExpression(interpreter.lisp.Expr, interpreter.lisp.Expr)
	 */
	@Override
	Expr evalBinaryExpression(Num value1, Num value2) {
		return new Num(value1.getValue()-value2.getValue());
	}

}
