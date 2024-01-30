package visitor;


public class VisitorTest {
	public static void main(String[] args) {
//		CountingVariablesVisitor v = new CountingVariablesVisitor();
		AbstractExpression expression = new Sum(new Minus(new Number(1),
				new Variable("x", 3)), new Sum(new Number(5), new Variable("y",
				7)));
		System.out.println(expression.toString());
//		expression.accept(v);
//		System.out.println(MessageFormat.format(
//				"There were {0} variables in the expression", v.getCount()));
		expression.accept(new PrintVisitor());
	}
}
