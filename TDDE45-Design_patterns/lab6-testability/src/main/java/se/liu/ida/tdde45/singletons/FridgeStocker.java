package se.liu.ida.tdde45.singletons;

import se.liu.ida.tdde45.house.Fridge;

public class FridgeStocker {
	protected boolean initialized = false;
	
	public void initialize() {
		initialized = true;
	}
	
	public void stock(Fridge fridge) throws UninitializedSingletonException {
		if(!initialized)
			throw new UninitializedSingletonException(FridgeStocker.class);
		
		OrderDispatcher.order();
		fridge.stock();
	}
}
