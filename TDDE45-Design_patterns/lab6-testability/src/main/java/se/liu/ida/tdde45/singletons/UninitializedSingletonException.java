package se.liu.ida.tdde45.singletons;

@SuppressWarnings("serial")
public class UninitializedSingletonException extends Exception {
	public UninitializedSingletonException(Class<?> singletonClass) {
		super("Singleton " + singletonClass.getName() + " has not been initialized!");
	}
}
