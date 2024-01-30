package se.liu.ida.tdde45;

import se.liu.ida.tdde45.house.Fridge;
import se.liu.ida.tdde45.singletons.FridgeStocker;
import se.liu.ida.tdde45.singletons.UninitializedSingletonException;

public class FridgeStockerSub extends FridgeStocker {

	@Override
	public void stock(Fridge fridge) throws UninitializedSingletonException {
		if(!super.initialized)
			throw new UninitializedSingletonException(FridgeStocker.class);
		
		fridge.stock();
	}
}
