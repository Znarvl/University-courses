package visitor;

import java.text.MessageFormat;

public class PrintVisitor extends Visitor {

	@Override
	public void visit(Number exp) {
		System.out.print(MessageFormat.format("{0} ", exp.getValue()));
	}

	@Override
	public void visit(Variable exp) {
		System.out.print(MessageFormat.format("{0} ", exp.getName()));
	}

	@Override
	public void visit(Sum exp) {
		System.out.print("+ ");
	}

	@Override
	public void visit(Minus exp) {
		System.out.print("- ");

	}

}
