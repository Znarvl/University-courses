package se.liu.ida.tdde45.house;

import se.liu.ida.tdde45.food.ingredients.Ingredient;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredient;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredientFactory;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredientFactory.InvalidIngredientException;

public class Workbench {
	public CookedIngredient process(Ingredient input) throws InvalidIngredientException {
		return CookedIngredientFactory.processIngredient(input);
	}
}
