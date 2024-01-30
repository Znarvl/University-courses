package interpreter.lisp;

import java.text.MessageFormat;

public class Num implements Expr {

	private int value;

	public Num(int value) {
		this.value = value;
	}

	public int getValue() {
		return value;
	}

	@Override
	public String toString() {
		return MessageFormat.format("{0}", value);
	}

	@Override
	public Expr evaluate(Context context) {
		return this;
	}
	
	@Override
	public boolean equals(Object obj) {
		boolean result = false;
		if (obj instanceof Num) {
			Num otherNum = (Num) obj;
			result = otherNum.getValue() == getValue();
		}
		return result;
	}
	
	@Override
	public int hashCode() {
		return getValue();
	}
	
}
