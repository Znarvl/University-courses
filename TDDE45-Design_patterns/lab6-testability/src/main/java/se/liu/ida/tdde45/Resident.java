package se.liu.ida.tdde45;

import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredient;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredientFactory.InvalidIngredientException;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredientFactory.UnknownIngredientException;
import se.liu.ida.tdde45.food.ingredients.raw.RawEgg;
import se.liu.ida.tdde45.food.ingredients.raw.RawPotato;
import se.liu.ida.tdde45.food.ingredients.raw.Yoghurt;
import se.liu.ida.tdde45.food.meals.Breakfast;
import se.liu.ida.tdde45.food.meals.Lunch;
import se.liu.ida.tdde45.house.Bed;
import se.liu.ida.tdde45.house.Bedroom;
import se.liu.ida.tdde45.house.Dresser;
import se.liu.ida.tdde45.house.Fridge;
import se.liu.ida.tdde45.house.Fridge.UnstockedException;
import se.liu.ida.tdde45.house.House;
import se.liu.ida.tdde45.house.Kitchen;
import se.liu.ida.tdde45.house.Stove.UnpoweredException;
import se.liu.ida.tdde45.singletons.FridgeStocker;
import se.liu.ida.tdde45.singletons.UninitializedSingletonException;


public class Resident {

	public Resident(){}

	public Resident(FridgeStocker f) throws UninitializedSingletonException{
		f.stock(this.house.getKitchen().getFridge());
	}

	public Resident(House house, FridgeStocker f) throws UninitializedSingletonException{
		this.house = house;
		f.stock(this.house.getKitchen().getFridge());
	}

	private House house = new House(new Bedroom(new Bed(), new Dresser()));
	private boolean sick = false;


	protected Breakfast makeBreakfast() throws UnknownIngredientException, UnpoweredException, UnstockedException {
		Kitchen kitchen = this.house.getKitchen();
		Fridge fridge = kitchen.getFridge();
		final RawEgg rawEgg = fridge.getEgg();
		final Yoghurt yoghurt = fridge.getYoghurt();
		//kitchen.getStove().turnOn();
		final Breakfast breakfast = new Breakfast(kitchen.getStove().boil(rawEgg), yoghurt);


		if(kitchen.getStove().isFilthy())
			sick = true;

		return breakfast;
	}

	protected Lunch makeLunch() throws InvalidIngredientException, UnknownIngredientException, UnpoweredException, UnstockedException {
		final RawEgg rawEgg = house.getKitchen().getFridge().getEgg();
		final RawPotato rawPotato = house.getKitchen().getFridge().getPotato();
		final CookedIngredient boiledPotato = house.getKitchen().getStove().boil(rawPotato);
		final Lunch lunch = new Lunch(house.getKitchen().getWorkbench().process(boiledPotato), house.getKitchen().getStove().boil(rawEgg));

		if(house.getKitchen().getStove().isFilthy())
			sick = true;

		return lunch;
	}

	public boolean isSick() {
		return sick;
	}
}
