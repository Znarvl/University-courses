package se.liu.ida.tdde45.house;

import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredient;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredientFactory;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredientFactory.UnknownIngredientException;
import se.liu.ida.tdde45.food.ingredients.raw.RawIngredient;

@SuppressWarnings("serial")
public class Stove {
	private boolean on = false;
	private boolean filthy = false;
	
	public void turnOn() {
		on = true;
	}

	public void turnOff() {
		on = false;
	}
	
	public boolean isOn() {
		return on;
	}
	
	public void setFilthy(boolean filthy) {
		this.filthy = filthy;
	}
	
	public boolean isFilthy() {
		return filthy;
	}
	
	public CookedIngredient boil(RawIngredient rawFood) throws UnknownIngredientException, UnpoweredException {
		if(!on)
			throw new UnpoweredException();
		
		return CookedIngredientFactory.createFromRaw(rawFood);
	}

	public static class UnpoweredException extends Exception {
		public UnpoweredException() {
			super("The stove has not been turned on!");
		}
	}
}
