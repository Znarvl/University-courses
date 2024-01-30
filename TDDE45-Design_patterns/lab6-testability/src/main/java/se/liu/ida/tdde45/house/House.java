package se.liu.ida.tdde45.house;

import se.liu.ida.tdde45.singletons.FridgeStocker;
import se.liu.ida.tdde45.singletons.UninitializedSingletonException;

public class House {
	final private Kitchen kitchen = new Kitchen();
	final private Bedroom bedroom;

	

	public House(Bedroom bedroom) {
		this.bedroom = bedroom;
	}

	public House(Bedroom bedroom, FridgeStocker fridgeStocker) throws UninitializedSingletonException {
		this.bedroom = bedroom;

		fridgeStocker.stock(this.kitchen.getFridge());
	}

	public Kitchen getKitchen() {
		return kitchen;
	}

	public Bedroom getBedroom() {
		return bedroom;
	}
}
