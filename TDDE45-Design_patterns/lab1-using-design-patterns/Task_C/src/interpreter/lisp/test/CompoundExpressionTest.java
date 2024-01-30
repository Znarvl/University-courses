package interpreter.lisp.test;

import static org.hamcrest.core.Is.is;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import interpreter.lisp.CompoundExpression;
import interpreter.lisp.Context;
import interpreter.lisp.Expr;
import interpreter.lisp.Num;
import interpreter.lisp.Reader;

import org.junit.Test;

public class CompoundExpressionTest {

	private static final String fac = "(def fac (x) (if (= x 0) 1 (* x (fac (- x 1)))))";
	private static final String applyFac = "(fac 5)";

	@Test
	public void testEvaluateFac() {
		Expr definition = Reader.read(fac).evaluate(Context.getTopLevelContext());
		assertThat(definition, is(instanceOf(CompoundExpression.class)));
	}
	
	@Test
	public void testEvaluateApplyFac() {
		Reader.read(fac).evaluate(Context.getTopLevelContext());
		Expr value = Reader.read(applyFac).evaluate(Context.getTopLevelContext());
		assertEquals(new Num(120), value);
	}

}
