package se.liu.ida.tdde45.house;

public class Kitchen {
	private final Stove stove = new Stove();
	private final Fridge fridge = new Fridge();
	private final Workbench workbench = new Workbench();
	
	public Stove getStove() {
		return stove;
	}
	
	public Fridge getFridge() {
		return fridge;
	}

	public Workbench getWorkbench() {
		return workbench;
	}
}
