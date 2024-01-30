package visitor;

public class Number extends SimpleExpression {
	private int value;

	public Number(int value) {
		super();
		this.value = value;
	}

	public int getValue() {
		return value;
	}

	@Override
	public String toString() {
		return String.valueOf(getValue());
	}

	@Override
	public void accept(Visitor v) {
		v.visit(this);
	}

}
