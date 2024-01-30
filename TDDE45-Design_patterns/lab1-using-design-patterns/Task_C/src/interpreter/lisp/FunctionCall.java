package interpreter.lisp;

import java.util.List;


public class FunctionCall extends CompoundExpression {

	private List<Expr> arguments;
	private Symbol fn;

	public FunctionCall(Symbol fn, List<Expr> subList) {
		this.fn = fn;
		this.arguments = subList;
	}

	@Override
	public Expr evaluate(Context context) {
		Fun definition = (Fun) context.get(fn);
		if (definition == null) {
			throw new Error("Lisp function ‘" + fn.toString() + "’ not found");
		}
		// Add a new stack frame for the function call
		Context newContext = new Context(context);
		List<Expr> args = this.arguments;
		List<Symbol> parameters = definition.getParameters();
		int index = 0;
		for (Expr expr : args) {
			Expr argument = expr.evaluate(context);
			newContext.put(parameters.get(index++), argument);
		}
		return definition.getBody().evaluate(newContext);
	}

}
