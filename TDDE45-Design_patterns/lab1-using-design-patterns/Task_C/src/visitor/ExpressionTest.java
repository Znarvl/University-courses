package visitor;

public class ExpressionTest {

	public static void main(String[] args) {
		AbstractExpression expression = new Sum(new Minus(new Number(1),
				new Variable("x", 3)), new Sum(new Number(5), new Variable("y",
				7)));
		System.out.println(expression);
	}

}
