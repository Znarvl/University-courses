package se.liu.ida.tdde45.singletons;

@SuppressWarnings("serial")
public class BankConnector {
	private static boolean initialized = false;
	
	public static void initialize() {
		initialized = true;
	}
	
	public static void withdraw() throws UninitializedSingletonException {
		if(!initialized)
			throw new UninitializedSingletonException(BankConnector.class);
		
		throw new OopsError();
	}

	public static class OopsError extends Error {
		public OopsError() {
			super("Oops! You just withdrew cash from a real bank account!");
		}
	}
}
