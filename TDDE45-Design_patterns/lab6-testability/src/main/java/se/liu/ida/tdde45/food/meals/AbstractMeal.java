package se.liu.ida.tdde45.food.meals;

import java.util.Arrays;
import java.util.List;

import se.liu.ida.tdde45.food.ingredients.Ingredient;

public abstract class AbstractMeal implements Meal {
	private final List<Ingredient> ingredients;
	public AbstractMeal(Ingredient... ingredients) {
		this.ingredients = Arrays.asList(ingredients);
	}
	
	public List<Ingredient> getIngredients() {
		return ingredients;
	}
}
