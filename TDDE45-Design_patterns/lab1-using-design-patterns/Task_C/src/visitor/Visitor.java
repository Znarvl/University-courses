package visitor;

import java.text.MessageFormat;

public abstract class Visitor {
	public abstract void visit(Number exp);

	public abstract void visit(Variable exp);

	public abstract void visit(Sum exp);

	public abstract void visit(Minus exp);

	public void visit(CompoundExpression compoundExpression) {
		System.err.print(MessageFormat.format("Wrong type of expression: {0}", compoundExpression));
	}

	public void visit(AbstractExpression expr) {
		System.err.print(MessageFormat.format("Wrong type of expression: {0}", expr));
	}

}
