package interpreter.lisp;

public enum Constants implements Expr {

	TRUE, FALSE, EMPTY_LIST;

	@Override
	public Expr evaluate(Context context) {
		return this;
	}
	
}
