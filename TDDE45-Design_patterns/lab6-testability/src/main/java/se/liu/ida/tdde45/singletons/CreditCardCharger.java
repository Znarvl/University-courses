package se.liu.ida.tdde45.singletons;

public class CreditCardCharger {
	private static boolean initialized = false;
	
	public static void initialize() {
		initialized = true;
	}
	
	public static void charge() throws UninitializedSingletonException {
		if(!initialized)
			throw new UninitializedSingletonException(CreditCardCharger.class);
		
		ChargingQueue.enqueue();
	}
}
