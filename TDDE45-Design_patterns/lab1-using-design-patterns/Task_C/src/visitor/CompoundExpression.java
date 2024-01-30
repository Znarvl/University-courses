package visitor;

import java.text.MessageFormat;

public abstract class CompoundExpression extends AbstractExpression {

	protected AbstractExpression leftOperand;
	protected AbstractExpression rightOperand;

	protected abstract String operator();

	@Override
	public String toString() {
		String formatString = "{0} " + operator() + " {1}";
		if (leftOperand instanceof CompoundExpression
				|| rightOperand instanceof CompoundExpression) {
			formatString = "({0}) " + operator() + " ({1})";
		}
		return MessageFormat.format(formatString, leftOperand, rightOperand);
	}




}
