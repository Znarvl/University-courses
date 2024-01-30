package se.liu.ida.tdde45.singletons;

public class OrderDispatcher {
	private static boolean initialized = false;
	
	public static void initialize() {
		initialized = true;
	}
	
	public static void order() throws UninitializedSingletonException {
		if(!initialized)
			throw new UninitializedSingletonException(OrderDispatcher.class);
		
		CreditCardCharger.charge();
	}
}
