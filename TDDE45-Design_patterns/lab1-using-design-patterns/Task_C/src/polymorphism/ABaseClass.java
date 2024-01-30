package polymorphism;

import java.text.MessageFormat;

public class ABaseClass {

	public void aMethod(ASubClass x) {
		System.out.println(MessageFormat.format(
				"ABaseClass.aMethod(ASubClass {0})", x));
	}

	public void aMethod(ABaseClass x) {
		System.out.println(MessageFormat.format(
				"ABaseClass.aMethod(ABaseClass {0})", x));
	}

	@Override
	public String toString() {
		return "'Base class object'";
	}

}
