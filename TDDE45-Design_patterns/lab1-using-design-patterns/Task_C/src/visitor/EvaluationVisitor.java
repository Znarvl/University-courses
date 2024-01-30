package visitor;

public class EvaluationVisitor extends Visitor {

	private int result;

	public int getResult() {
		return result;
	}

	@Override
	public void visit(Number exp) {
		result = exp.getValue();
	}

	@Override
	public void visit(Variable exp) {
		result = exp.getValue();
	}

	@Override
	public void visit(Sum exp) {
		// result = ??
	}

	@Override
	public void visit(Minus exp) {
		// result = ??
	}


}
