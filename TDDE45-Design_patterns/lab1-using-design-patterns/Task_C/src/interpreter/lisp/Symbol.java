package interpreter.lisp;

import java.text.MessageFormat;

public class Symbol implements Expr {

	private String value;

	public Symbol(String elt) {
		this.value = elt;
	}

	public String getValue() {
		return value;
	}

	@Override
	public String toString() {
		return MessageFormat.format("{0}", value);
	}

	@Override
	public Expr evaluate(Context context) {
		return context.get(this);
	}
	
	@Override
	public boolean equals(Object obj) {
		return obj.getClass() == Symbol.class && ((Symbol)obj).value.equals(value);
	}
	
	@Override
	public int hashCode() {
		return value.hashCode();
	}
	
}
