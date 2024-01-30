package se.liu.ida.tdde45.singletons;

@SuppressWarnings("serial")
public class BankConnectorMock {
	private boolean initialized = false;
	
	public void initialize() {
		initialized = true;
	}
	
	public void withdraw() throws UninitializedSingletonException {
		if(!initialized)
			throw new UninitializedSingletonException(BankConnectorMock.class);
	}


}
