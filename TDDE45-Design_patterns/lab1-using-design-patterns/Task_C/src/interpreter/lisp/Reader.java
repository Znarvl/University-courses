package interpreter.lisp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Reader {

	/**
	 * 
	 * All expressions are either atomic (numbers, variables) or compound
	 * expressions (function definitions, conditional if-expressions, function
	 * calls). This method creates an Expr object from such a string.
	 * 
	 * @param expression
	 * @return
	 */
	public static Expr read(String expression) {

		/*
		 * Replaces parentheses with parentheses surrounded by spaces, to
		 * enable clean split-on-whitespace functionality
		 */
		expression = expression.replaceAll("\\(", " ( ").replaceAll("\\)",
				" ) ");

		List<String> l = new ArrayList<String>();
		l.addAll(Arrays.asList(expression.split("\\s+")));
		// Trim the list
		l.removeAll(Arrays.asList(""));
		return read(l);
	}

	/**
	 * Create an abstract expression, either a compound term or an atom, from a
	 * list of tokens
	 * 
	 * @param arr
	 * @return
	 */
	private static Expr read(List<String> arr) {
		Expr result = null;

		String elt = "";
		elt = arr.get(0);
		arr.remove(0);
		if (elt.equals("(")) {
			CompoundExpression compoundNode = new CompoundExpression();
			while (!arr.isEmpty() && !arr.get(0).equals(")")) {
				compoundNode.add(read(arr));
			}
			if (!arr.isEmpty()) {
				arr.remove(0);
			}
			result = compoundNode;
		} else if (elt.matches("\\d+")) {
			result = new Num(Integer.parseInt(elt));
		} else {
			result = new Symbol(elt);
		}
		return result;
	}

}
