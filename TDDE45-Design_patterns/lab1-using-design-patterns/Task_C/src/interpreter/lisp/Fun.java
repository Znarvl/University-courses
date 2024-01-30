package interpreter.lisp;

import java.util.List;

public interface Fun {

	public abstract List<Symbol> getParameters();

	public abstract Expr getBody();

}