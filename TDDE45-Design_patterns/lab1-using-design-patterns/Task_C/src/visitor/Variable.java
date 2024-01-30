package visitor;

public class Variable extends SimpleExpression {
	private String name;
	private int value;

	public Variable(String name, int value) {
		super();
		this.name = name;
		this.value = value;
	}

	public String getName() {
		return name;
	}

	public int getValue() {
		return value;
	}

	@Override
	public String toString() {
		return getName();
	}

	@Override
	public void accept(Visitor v) {
		v.visit(this);
	}
	
	
}
