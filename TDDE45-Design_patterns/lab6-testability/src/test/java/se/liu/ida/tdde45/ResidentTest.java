package se.liu.ida.tdde45;

import org.testng.annotations.Test;
import org.testng.Assert;
import se.liu.ida.tdde45.food.ingredients.cooked.CookedIngredientFactory.UnknownIngredientException;
import se.liu.ida.tdde45.house.Bed;
import se.liu.ida.tdde45.house.Bedroom;
import se.liu.ida.tdde45.house.Dresser;
import se.liu.ida.tdde45.house.House;
import se.liu.ida.tdde45.house.Stove;
import se.liu.ida.tdde45.house.Fridge.UnstockedException;
import se.liu.ida.tdde45.house.Stove.UnpoweredException;
import se.liu.ida.tdde45.singletons.BankConnector;
import se.liu.ida.tdde45.singletons.BankConnectorMock;
import se.liu.ida.tdde45.singletons.ChargingQueue;
import se.liu.ida.tdde45.singletons.CreditCardCharger;
import se.liu.ida.tdde45.singletons.FridgeStocker;
import se.liu.ida.tdde45.singletons.OrderDispatcher;
import se.liu.ida.tdde45.singletons.UninitializedSingletonException;

public class ResidentTest {
	
	@Test
	public void testMakeBreakfast() throws UnknownIngredientException, UnpoweredException, UnstockedException, UninitializedSingletonException{
		FridgeStockerSub fridgeStocker = new FridgeStockerSub();
		fridgeStocker.initialize();

		/*
		OrderDispatcher orderDispatcher = new OrderDispatcher();
		orderDispatcher.initialize();

		CreditCardCharger creditCardCharger = new CreditCardCharger();
		creditCardCharger.initialize();

		ChargingQueue chargingQueue = new ChargingQueue();
		chargingQueue.initialize();

		BankConnectorMock bankConnectorMock = new BankConnectorMock();
		bankConnectorMock.initialize();
		*/
		House house = new House(new Bedroom(new Bed(), new Dresser()));
		Resident r = new Resident(house, fridgeStocker);
		Stove stove = house.getKitchen().getStove();
		stove.turnOn();
		r.makeBreakfast();

	}

	
	
	/*
	@Test(expectedExceptions = UninitializedSingletonException.class)
	public void testMakeBreakfastFailsIfFridgeStockerIsNotInitialized() throws UnknownIngredientException, UnpoweredException, UnstockedException, UninitializedSingletonException{
		FridgeStockerSub fridgeStocker = new FridgeStockerSub();

		
		OrderDispatcher orderDispatcher = new OrderDispatcher();
		orderDispatcher.initialize();

		CreditCardCharger creditCardCharger = new CreditCardCharger();
		creditCardCharger.initialize();

		ChargingQueue chargingQueue = new ChargingQueue();
		chargingQueue.initialize();

		BankConnectorMock bankConnectorMock = new BankConnectorMock();
		bankConnectorMock.initialize();
		
	
		Resident r = new Resident(fridgeStocker);
		r.makeBreakfast();
	
	}
	*/


	@Test
	public void cookingOnAFilthyStove() throws UnknownIngredientException, UnpoweredException, UnstockedException, UninitializedSingletonException {
		FridgeStockerSub fridgeStocker = new FridgeStockerSub();
		fridgeStocker.initialize();

		House house = new House(new Bedroom(new Bed(), new Dresser()));
		Resident r = new Resident(house, fridgeStocker);
		Stove stove = house.getKitchen().getStove();
		stove.setFilthy(true);
		stove.turnOn();
		r.makeBreakfast();
		Assert.assertEquals(r.isSick(), true);
		
			
	} 

	@Test(expectedExceptions = UnpoweredException.class)
	public void cookingOnAFilthyStoveNotTurnedOn() throws UnknownIngredientException, UnpoweredException, UnstockedException, UninitializedSingletonException {
		FridgeStockerSub fridgeStocker = new FridgeStockerSub();
		fridgeStocker.initialize();

		House house = new House(new Bedroom(new Bed(), new Dresser()));
		Resident r = new Resident(house, fridgeStocker);
		r.makeBreakfast();
		Assert.assertEquals(r.isSick(), false);
		
			
	} 

}
