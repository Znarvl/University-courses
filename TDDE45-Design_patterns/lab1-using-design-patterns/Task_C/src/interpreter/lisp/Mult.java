package interpreter.lisp;

public class Mult extends BinaryExpression<Num> {

	@Override
	Expr evalBinaryExpression(Num value1, Num value2) {
		return new Num(value1.getValue()*value2.getValue());
	}

}
