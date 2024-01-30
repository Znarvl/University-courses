package se.liu.ida.tdde45.food.ingredients.cooked;

import se.liu.ida.tdde45.food.ingredients.Ingredient;
import se.liu.ida.tdde45.food.ingredients.raw.RawEgg;
import se.liu.ida.tdde45.food.ingredients.raw.RawIngredient;
import se.liu.ida.tdde45.food.ingredients.raw.RawPotato;

@SuppressWarnings("serial")
public class CookedIngredientFactory {
	public static CookedIngredient createFromRaw(RawIngredient raw) throws UnknownIngredientException {
		if(raw instanceof RawEgg)
			return new BoiledEgg();
		
		if(raw instanceof RawPotato)
			return new BoiledPotato();
		
		throw new UnknownIngredientException(raw);
	}
	
	public static CookedIngredient processIngredient(Ingredient ingredient) throws InvalidIngredientException {
		if(ingredient instanceof BoiledPotato)
			return new MashedPotato();
		
		throw new InvalidIngredientException(ingredient);
	}
	
	public static class UnknownIngredientException extends Exception {
		public UnknownIngredientException(RawIngredient raw) {
			super("Unknown ingredient: " + raw.getClass());
		}
	}

	public static class InvalidIngredientException extends Exception {
		public InvalidIngredientException(Ingredient ingredient) {
			super("Ingredient invalid for processing: " + ingredient.getClass());
		}
	}
}
