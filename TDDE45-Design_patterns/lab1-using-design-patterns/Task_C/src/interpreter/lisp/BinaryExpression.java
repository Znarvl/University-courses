package interpreter.lisp;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * All built-in functions are represented using this class. We declare to
 * virtual parameters "param1" and "param2" for all binary functions.
 * 
 * @author olale
 * 
 */
public abstract class BinaryExpression<T extends Expr> implements Expr, Fun {

	private static Symbol param1 = new Symbol("param1");
	private static Symbol param2 = new Symbol("param2");
	private static ArrayList<Symbol> parameters;

	static {
		parameters = new ArrayList<Symbol>();
		parameters.add(param1);
		parameters.add(param2);
	}

	@SuppressWarnings("unchecked")
	@Override
	public Expr evaluate(Context context) {
		T value1 = (T) context.get(param1);
		T value2 = (T) context.get(param2);
		return evalBinaryExpression(value1, value2);
	}

	abstract Expr evalBinaryExpression(T value1, T value2);

	@Override
	public List<Symbol> getParameters() {
		return parameters;
	}

	@Override
	public Expr getBody() {
		return this;
	}

}