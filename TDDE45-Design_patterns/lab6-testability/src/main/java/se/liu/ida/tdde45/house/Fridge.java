package se.liu.ida.tdde45.house;

import se.liu.ida.tdde45.food.ingredients.raw.RawEgg;
import se.liu.ida.tdde45.food.ingredients.raw.RawPotato;
import se.liu.ida.tdde45.food.ingredients.raw.Yoghurt;

@SuppressWarnings("serial")
public class Fridge {

	private boolean stocked = false;

	public RawEgg getEgg() throws UnstockedException {
		if(!stocked)
			throw new UnstockedException();

		return new RawEgg();
	}

	public Yoghurt getYoghurt() throws UnstockedException {
		if(!stocked)
			throw new UnstockedException();

		return new Yoghurt();
	}

	public RawPotato getPotato() throws UnstockedException {
		if(!stocked)
			throw new UnstockedException();

		return new RawPotato();
	}

	public void stock() {
		this.stocked = true;

	}

	public static class UnstockedException extends Exception {
		public UnstockedException() {
			super("Fridge has not been stocked!");
		}
	}
}
