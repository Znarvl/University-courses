package interpreter.lisp;

import java.util.ArrayList;
import java.util.List;

public class CompoundExpression implements Expr {

	private List<Expr> elements = new ArrayList<Expr>();

	public void add(Expr node) {
		elements.add(node);
	}

	public List<Expr> getElements() {
		return elements;
	}

	public Expr evaluate(Context context) {
		if (elements.isEmpty()) {
			return Constants.EMPTY_LIST;
		}
		if (elements.get(0) instanceof Symbol) {
			String keyword = ((Symbol) elements.get(0)).getValue();
			if (keyword.equals("def")) {
				return new CompoundFunction(elements.get(1), elements.get(2),
						elements.get(3)).evaluate(context);
			} else if (keyword.equals("if")) {
				return new Conditional(elements.get(1), elements.get(2),
						elements.get(3)).evaluate(context);
			}
		}
		return new FunctionCall((Symbol) elements.get(0),elements.subList(1,elements.size())).evaluate(context);
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		List<Expr> e = elements;
		sb.append("[");
		for (Expr node : e) {
			sb.append(node);
			sb.append(" ");
		}
		sb.append("]");
		return sb.toString();
	}


}
