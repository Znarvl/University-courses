package interpreter.lisp;

import java.util.HashMap;

public class Context {

	public HashMap<Symbol, Expr> bindings = new HashMap<Symbol, Expr>();
	private Context parent;

	private static Context topLevelContext = new Context();
	private static final Context TOP_LEVEL_CONTEXT = topLevelContext;
	
	private Context() {
		bindings.put(new Symbol("="), new Eq());
		bindings.put(new Symbol("*"), new Mult());
		bindings.put(new Symbol("-"), new Sub());
		// Add new top level bindings here
	}
	
	public Context(Context parent) {
		this.parent=parent;
	}
	
	public Expr get(Symbol var) {
		Expr value = bindings.get(var);
		if (value == null && hasParent()) {
			value = getParent().get(var);
		}
		return value;
	}

	public void put(Symbol key, Expr value) {
		bindings.put(key, value);
	}

	@Override
	public String toString() {
		return bindings.toString();
	}

	public void extend(Context context) {
		this.parent = context;
	}

	public Context getParent() {
		return parent;
	}
	
	public boolean hasParent() {
		return parent != null;
	}

	public static Context getTopLevelContext() {
		return TOP_LEVEL_CONTEXT;
	}
	
}
