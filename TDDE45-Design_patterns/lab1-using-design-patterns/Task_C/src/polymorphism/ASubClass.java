package polymorphism;

import java.text.MessageFormat;

public class ASubClass extends ABaseClass {

	public void aMethod(ASubClass x) {
		System.out.println(MessageFormat.format(
				"ASubClass.aMethod(ASubClass {0})", x));
	}

	public void aMethod(ABaseClass x) {
		System.out.println(MessageFormat.format(
				"ASubClass.aMethod(ABaseClass {0})", x));
	}

	@Override
	public String toString() {
		return "'Subclass object'";
	}

}
