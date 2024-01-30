package interpreter.lisp;

public class Conditional extends CompoundExpression {

	private Expr condition;
	private Expr consequent;
	private Expr antecedent;

	public Conditional(Expr condition, Expr consequent, Expr antecedent) {
		this.condition = condition;
		this.consequent = consequent;
		this.antecedent = antecedent;
	}

	public Expr getCondition() {
		return condition;
	}

	public Expr getConsequent() {
		return consequent;
	}

	public Expr getAntecedent() {
		return antecedent;
	}

	@Override
	public Expr evaluate(Context context) {
		return condition.evaluate(context) == Constants.TRUE ? consequent
				.evaluate(context) : antecedent.evaluate(context);
	}

}
