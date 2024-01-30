package interpreter.lisp.test;

import static org.junit.Assert.assertEquals;
import interpreter.lisp.CompoundExpression;
import interpreter.lisp.Num;
import interpreter.lisp.Reader;
import interpreter.lisp.Symbol;

import org.junit.Test;

public class ReaderTest {

	@Test
	public void testReadFunctionDefinition() {
		String functionDefinition = "(def fac (x) (if (= x 0) 1 (* x (fac (- x 1)))))";
		assertEquals(CompoundExpression.class, Reader.read(functionDefinition).getClass());
	}
	
	@Test
	public void testReadSimpleExpression() {
		assertEquals(new Num(1), Reader.read("1"));
	}

	@Test
	public void testReadVariable() {
		assertEquals(new Symbol("x"), Reader.read("x"));
	}
	
	
}
